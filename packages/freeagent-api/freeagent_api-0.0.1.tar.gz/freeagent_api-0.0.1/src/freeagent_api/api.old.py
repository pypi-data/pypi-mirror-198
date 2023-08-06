"""Python module for interacting with the FreeAgent accounting software API.

Currently limited to invoice related stuff.
"""
import sys
import os
from datetime import datetime
from time import sleep
import logging
import requests
from colorlog import ColoredFormatter
import freeagent_api


SANDBOX_API_BASE = 'https://api.sandbox.freeagent.com/v2'
PRODUCTION_API_BASE = 'https://api.freeagent.com/v2'

# Maximum number of attempts to contact the API if rate limiting occurs
MAX_RETRIES = 5


class ApiClient:
    """Main API client class.

    This is the main API for interacting with the FreeAgent API. it's currently
    limited to obtaining invoices and related data. Note that you will need to
    call do_auth() or load a serialised authentication token into the
    serialised_token attribute for API calls to work. All data returned will be
    from the authenticated user's account.

    Rate limiting will be handled automatically if too many requests are made in
    a short time (see https://dev.freeagent.com/docs/introduction for the
    limits) by waiting as advised by the API.

    The environment variable 'LOG_LEVEL' can be set to 'DEBUG, 'INFO',
    'WARNING', 'ERROR', or 'CRITICAL' to limit display of log messages. The
    default is 'INFO'.
    """

    def __init__(self, client_id: str, client_secret: str, use_sandbox: bool = False):
        """Initialise the instance.

        Args:
            client_id (str): Client ID for your app.
            client_secret (str): Client secret for your app.
            use_sandbox (bool, optional): Whether to use the sandbox or production system. Defaults
                to False, meaning to use the production system.
        """
        self.use_sandbox = use_sandbox

        if use_sandbox:
            self.api_base = SANDBOX_API_BASE
        else:
            self.api_base = PRODUCTION_API_BASE

        # Initialise a logger
        self.logger = logging.getLogger(__name__)
        log_handler = logging.StreamHandler(sys.stdout)
        log_formatter = ColoredFormatter(
            fmt="%(log_color)s%(asctime)s %(name)s: [%(levelname)s] %(message)s%(reset)s",
            datefmt="%b %d %H:%M:%S",
            log_colors={
                'DEBUG':    'black',
                'INFO':     'reset',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',
            },
        )
        log_handler.setFormatter(log_formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(os.environ.get("LOG_LEVEL", "DEBUG"))

        self.oauth = freeagent_api.OAuthHandler(client_id, client_secret, use_sandbox)


    def do_auth(self):
        """Get an authentication token for the users's account.

        Just a pass-through function to the OAuthHandler instance.
        """
        self.oauth.do_auth()


    @property
    def serialised_token(self) -> str:
        """Serialise the authentications for storage.

        Just a pass-through function to the OAuthHandler instance.

        Returns:
            str: storable tokens
        """
        return self.oauth.serialised_token

    @serialised_token.setter
    def serialised_token(self, value: str):
        self.oauth.serialised_token = value


    def _get(self, endpoint: str, params: dict = None) -> dict:
        """Wrapper around requests.get.

        Args:
            endpoint (str): API endpoint to access. Note: Base url of
                'https://api.(sandbox.)freeagent.com/v2' will be added
                automatically.

        Returns:
            dict: Request response as decoded JSON object
        """
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint

        #print("GET", self.api_base + endpoint)
        #print("with params", params)

        self.oauth.refresh_token_if_necessary()
        response = None
        retries = MAX_RETRIES
        while retries > 0:
            response = requests.get(
                self.api_base + endpoint,
                headers = { "Authorization": self.oauth.authorisation_header },
                timeout = 10,
                params = params,
            )

            if 'retry-after' in response.headers:
                self.logger.info(
                    "Hit API rate limit, waiting %s seconds before retrying",
                    response.headers['Retry-After'],
                )
                retries -= 1
                if retries > 0:
                    sleep(int(response.headers['retry-after']))
                else:
                    raise RuntimeError(f"Failed to get API response after {MAX_RETRIES} retries due to rate limiting")

            else:
                break

        #TODO: Parse 'Link' header to get additional pages of results
        #if 'link' in response.headers and response.headers['link'] != "":
        #    print("link:", response.headers['Link'])

        return response.json()


    def get_company(self) -> freeagent_api.Company:
        """Get information about the company.

        Returns:
            freeagent_api.Company: Company data.
        """
        data = self._get('/company')['company']
        if self.use_sandbox:
            data['subdomain'] += ".sandbox"
        return freeagent_api.Company(data)


    def get_user(self) -> freeagent_api.User:
        """Get information about the currently authorised user.

        Returns:
            freeagent.User: User data.
        """
        data = self._get('/users/me')['user']
        return freeagent_api.User(data)


    def get_contact(self, contact_id: int) -> freeagent_api.Contact:
        """Get information about a contact.

        Args:
            contact_id (int): ID of the contact. Typically obtained from the
                contact field of a freeagent.Invoice object or similar.

        Returns:
            freeagent_api.Contact: Contact data.
        """
        data = self._get(f'/contacts/{int(contact_id)}')
        return freeagent_api.Contact(data.get('contact'))


    def get_invoices(self,
        status: str = "all",
        within_months: int = None,
        updated_since: datetime = None,
        sort_order: str = "created_at"
    ) -> list[freeagent_api.Invoice]:
        """Get a list of invoices with their associated data.

        All invoices will automatically have their line item data included.

        Args:
            status (str, optional): Status of invoices to get. Valid values are:
                - all: Show all invoices.
                - recent_open_or_overdue: Show only recent, open, or overdue invoices.
                - open: Show only open invoices.
                - overdue: Show only overdue invoices.
                - open_or_overdue: Show only open or overdue invoices.
                - draft: Show only draft invoices.
                - paid: Show only paid invoices.
                - scheduled_to_email: Show only invoices scheduled to email.
                - thank_you_emails: Show only invoices with active thank you emails.
                - reminder_emails: Show only invoices with active reminders.
                - last_N_months: Show only invoices from the last N months.
                Defaults to "all". Cannot be specified at the same time as 'within_months'.
            within_months (int, optional): Maximum age of the invoice in months. Cannot be specified
                at the same time as 'status'. Defaults to None.
            updated_since (datetime, optional): Only return invoices updated since this timestamp.
                Defaults to None, meaning no limit.
            sort_order (str, optional): Order to return results in. Valid values are:
                - created_at: Sort by the time the invoice was created.
                - updated_at: Sort by the time the invoice was last modified.
                Defaults to "created_at".

        Returns:
            list[freeagent_api.Invoice]: List of invoices.
        """
        if status not in ["all", "recent_open_or_overdue", "open", "overdue",
                          "open_or_overdue", "draft", "paid", "scheduled_to_email",
                          "thank_you_emails", "reminder_emails"]:
            raise ValueError("Invalid status for invoice request")
        if within_months is not None and status != "all":
            raise ValueError("Cannot specify both status and within_months for getting invoices")
        if sort_order not in ["created_at", "updated_at", "-created_at", "-updated_at"]:
            raise ValueError("Invalid sort order for invoice request")

        request_params = {
            'nested_invoice_items': True,
            'sort': sort_order,
        }
        if updated_since is not None:
            request_params['updated_since'] = updated_since.isoformat()

        if within_months is not None:
            request_params['view'] = f"last_{within_months}_months"
        else:
            request_params['view'] = status

        data = self._get('/invoices', request_params)

        invoices = []
        for data_invoice in data.get('invoices'):
            invoice = freeagent_api.Invoice(data_invoice)
#            invoice.invoice_items = []
#            for data_invoice_item in data_invoice.get('invoice_items'):
#                invoice.invoice_items.append(freeagent.InvoiceItem(data_invoice_item))
            invoices.append(invoice)

        return invoices


    def get_bank_account(self, account_id: int) -> freeagent_api.BankAccount:
        """Get bank account data.

        Args:
            account_id (int): ID of the account. Typically obtained from the
                bank_account field of a freeagent.Invoice object or similar.

        Returns:
            freeagent_api.BankAccount: Bank account data.
        """
        data = self._get(f'/bank_accounts/{int(account_id)}')
        return freeagent_api.BankAccount(data.get('bank_account'))
