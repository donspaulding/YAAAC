import urllib, urllib2

CLIENT_LOGIN_URL = 'https://www.google.com/accounts/ClientLogin'

def do_clientlogin(email, password, account_type, service, url=CLIENT_LOGIN_URL):
    """
    Submit a request to Google's ClientLogin service for installed applications.
    """
    data = urllib.urlencode({
        'Email': email,
        'Passwd': password,
        'accountType': account_type,
        'service': service,
    })
    try:
        resp = urllib2.urlopen(url, data)
        return dict((l.split('=', 1) for l in resp.read().splitlines()))
    except urllib2.HTTPError, e:
        raise RuntimeError(e.read())

def get_adwords_auth(email, password):
    return do_clientlogin(email, password, account_type='GOOGLE', service='adwords')['Auth']
