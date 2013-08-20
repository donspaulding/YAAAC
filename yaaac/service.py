import time
import datetime

import suds
from suds.client import Client
from yaaac.auth import get_adwords_auth

VERSION = "0.4.0"


class WebService(object):
    def __init__(self, url):
        self._wrapped_client = Client(url)
        self._cached_references = {}

    def __getattr__(self, name):
        if name in self._cached_references:
            return self._cached_references[name]
        try:
            new_reference = self.method_wrapper(getattr(self._wrapped_client.service, name))
        except suds.MethodNotFound:
            svc = self

            class ServiceType(object):
                def __new__(cls, **kwargs):
                    obj = svc._wrapped_client.factory.create(name)
                    for k, v in kwargs.items():
                        setattr(obj, k, v)
                    return obj
            ServiceType.__name__ = name
            new_reference = ServiceType
        self._cached_references[name] = new_reference
        return new_reference

    def method_wrapper(self, suds_method):
        return suds_method

class NewAdwordsService(WebService):
    def method_wrapper(self, suds_method):
        def wrapped(*args, **kwargs):
            headers = self.SoapHeader(

            )
            suds_method.client.set_options(
            )


class CallbackMethod:
    def __init__(self, method, callback):
        self.method = method
        self.callback = callback

    def __call__(self, *args, **kwargs):
        self.callback(client_email=kwargs.pop('client_email', ''), client_id=kwargs.pop('client_id', ''))
        return self.method(*args, **kwargs)

    def __repr__(self):
        return repr(self.method)

    def __str__(self):
        return str(self.method)


class AdwordsService(suds.client.Client):
    _token_cache = {}
    _token_expirations = {}

    def __init__(self, url, email, password, developer_token, user_agent="YAAAC Client (%s)" % VERSION,
                    auth_token_lifetime=datetime.timedelta(days=1), debug=False, request_delay=None):
        super(AdwordsService, self).__init__(url)
        self._debug = debug
        self._email = email
        self._password = password
        self._developer_token = developer_token
        self._user_agent = user_agent
        self._auth_token_lifetime = auth_token_lifetime
        self._wrapped_methods = {}
        ###  AdWords auth tokens from the ClientLogin service are only
        ###  valid for "about one week".  The auth_token_lifetime needs
        ###  to be a datetime.timedelta that is less than that.
        ###   ...  http://code.google.com/apis/adwords/v2009/docs/headers.html
        self._reset_auth_token()  # Prime the token_cache

    def _reset_auth_token(self):
        self._token_cache[self._email] = get_adwords_auth(self._email, self._password)
        self._token_expirations[self._email] = datetime.datetime.now() + self._auth_token_lifetime

    def _set_adwords_headers(self, client_email='', client_id=''):
        head = self.factory.create("SoapHeader")
        head.authToken = self._token_cache[self._email]
        head.developerToken = self._developer_token
        head.userAgent = self._user_agent
        if client_id:
            head.clientCustomerId = client_id
        elif client_email:
            head.clientEmail = client_email
        self.set_options(soapheaders=head)

    def __getattr__(self, attr):
        if datetime.datetime.now() > self._token_expirations[self._email]:
            self._reset_auth_token()
        try:
            method = getattr(self.service, attr)
        except suds.MethodNotFound:
            method = None
        if method and callable(method):
            return CallbackMethod(method, callback=self._set_adwords_headers)
        return getattr(super(AdwordsService, self), attr)
