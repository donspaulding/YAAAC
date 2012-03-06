import time
import datetime

import suds
from yaaac.auth import get_adwords_auth

VERSION = "0.3.1"


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
        self._request_delay = request_delay
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
        if self._request_delay is not None:
            time.sleep(self._request_delay)
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
