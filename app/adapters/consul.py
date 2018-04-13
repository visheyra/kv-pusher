import requests
import uritools
import json
from base64 import b64decode


class Consul:
    def configure(self, endpoint, port):
        self.endpoint = endpoint
        self.port = port
        self.session = requests.Session()

    def _path_in_url(self, key):
        return uritools.uricompose(
            scheme='http',
            host=self.endpoint,
            port=self.port,
            path='/v1/kv/{}'.format(key.lstrip('/'))
        )

    def write(self, key, value, verbosity=False):
        try:
            r = self.session.put(self._path_in_url(key), data=value)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e.args[0].args[0])
        if verbosity:
            print(r.text)
        if r.status_code != 200:
            raise RuntimeError('Write did not succeed')
        elif verbosity:
            print('succeeds')

    def delete(self, key, value, verbosity=False):
        try:
            r = self.session.delete(self._path_in_url(key))
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e.args[0].args[0])
        if verbosity:
            print(r.text)
        if r.status_code != 200:
            raise RuntimeError('Delete did not succeed')
        elif verbosity:
            print('succeeds')

    def read(self, key, value, verbosity):
        try:
            r = self.session.get(self._path_in_url(key))
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e.args[0].args[0])
        if verbosity:
            print(json.dumps(r.json(), indent=2))
        if r.status_code != 200:
            raise RuntimeError('Read did not succeed')
        elif verbosity:
            print('succeeds')
        return b64decode(r.json()[0]["Value"]).decode('utf-8')

    def do(self, action, key, value, verbosity):
        return {
            'read': self.read,
            'write': self.write,
            'delete': self.delete
        }[action](key, value, verbosity)
