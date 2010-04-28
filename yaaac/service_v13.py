from suds.client import Client as SudsClient
from yaaac import VERSION, MIN_API_VERSION, SERVICES

class Client(object):
    def __init__(self, email=None, password=None, app_token=None, dev_token=None, user_agent="YAAAC Client (%s)"%VERSION, client_email=None, client_customer_id=None, api_version=MIN_API_VERSION):
        self.email = email
        self.password = password
        self.app_token = app_token
        self.dev_token = dev_token
        self.user_agent = user_agent
        if client_email is not None:
            self.client_email = client_email
        if client_customer_id is not None:
            self.client_customer_id = client_customer_id
        self.api_version = api_version
        self.wsdl_urls = {}
        for service in SERVICES:
            self.wsdl_urls[service] = 'https://adwords.google.com/api/adwords/v%s/%s?wsdl'%(self.api_version, service)

    def _get_client_email(self):
        return self._client_email

    def _set_client_email(self, value):
        self._client_customer_id = None
        self._client_email = value
    client_email = property(_get_client_email, _set_client_email)

    def _get_client_customer_id(self):
        return self._client_customer_id

    def _set_client_customer_id(self, value):
        self._client_email = None
        self._client_customer_id = value
    client_customer_id = property(_get_client_customer_id, _set_client_customer_id)

    def get_service(self, name):
        c = SudsClient(self.wsdl_urls[name])
        c.set_options(soapheaders={
                    'email'     :   self.email,
                    'password'  :   self.password,
                    'applicationToken'  :   self.app_token,
                    'developerToken'    :   self.dev_token,
                    'useragent'         :   self.user_agent,
                    }
        )
        return c

    def __getattr__(self, name):
        if name.endswith("Service"):
            return self.get_service(name)
        return getattr(self, name)
