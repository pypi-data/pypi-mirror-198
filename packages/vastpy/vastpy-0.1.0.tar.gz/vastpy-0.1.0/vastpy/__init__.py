from urllib3.exceptions import InsecureRequestWarning
import urllib3
import http
import json

class RESTFailure(Exception): pass
SUCCESS_CODES = {http.HTTPStatus.OK,
                 http.HTTPStatus.CREATED,
                 http.HTTPStatus.ACCEPTED,
                 http.HTTPStatus.NON_AUTHORITATIVE_INFORMATION,
                 http.HTTPStatus.NO_CONTENT,
                 http.HTTPStatus.RESET_CONTENT,
                 http.HTTPStatus.PARTIAL_CONTENT}

class VASTClient(object):
    def __init__(self, user, password, address, url='api', cert_file=None, cert_server_name=None):
        self._user = user
        self._password = password
        self._address = address
        self._cert_file = cert_file
        self._cert_server_name = cert_server_name
        self._url = url

    def __getattr__(self, part):
        return self[part]

    def __getitem__(self, part):
        return self.__class__(user=self._user,
                              password=self._password,
                              address=self._address,
                              cert_file=self._cert_file,
                              cert_server_name=self._cert_server_name,
                              url=f'{self._url}/{part}')

    def __repr__(self):
        return f'VASTClient(address="{self._address}", url="{self._url}")'

    def request(self, method, params):
        if self._cert_file:
            pm = urllib3.PoolManager(ca_certs=self._cert_file, server_hostname=self._cert_server_name)
        else:
            pm = urllib3.PoolManager(cert_reqs='CERT_NONE')
            urllib3.disable_warnings(category=InsecureRequestWarning)
        headers = urllib3.make_headers(basic_auth=self._user + ':' + self._password)
        r = pm.request(method, f'https://{self._address}/{self._url}/', headers=headers, fields=params)
        if r.status not in SUCCESS_CODES:
            raise RESTFailure(f'Response for request {method} {self._url} with {params} failed with error {r.status} and message {r.data}')
        data = r.data
        if data:
            return json.loads(data.decode('utf-8'))

    def get(self, **params):
        return self.request('GET', params)
    def post(self, **params):
        return self.request('POST', params)
    def put(self, **params):
        return self.request('PUT', params)
    def patch(self, **params):
        return self.request('PATCH', params)
    def options(self, **params):
        return self.request('OPTIONS', params)
    def delete(self, **params):
        return self.request('DELETE', params)
