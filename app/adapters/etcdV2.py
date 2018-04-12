import requests
import uritools
import json

class EtcdV2:

    def configure(self, endpoint, port):
        self.endpoint = endpoint
        self.port = port
        self.session = requests.Session()

    def _path_in_url(self, key):
        return uritools.uricompose(
            scheme='http',
            host=self.endpoint,
            port=self.port,
            path='/v2/keys/{}'.format(key.lstrip('/'))
        )

    def write(self, key, value, verbosity=False):
        r = self.session.put(self._path_in_url(key), data={ 'value': value })
        if verbosity:
            print(json.dumps(r.json(), indent=2))
        if r.status_code != 200:
            raise RuntimeError('Did not succeed')
        elif verbosity:
            print('succeeds')

    def delete(self, key, value, verbosity=False):
        r = self.session.delete(self._path_in_url(key))
        if verbosity:
            print(json.dumps(r.json(), indent=2))
        if r.status_code != 200:
            raise RuntimeError('Did not succeed')
        elif verbosity:
            print('succeeds')

    def update(self, key, value, verbosity=False):
        self.write(key, value, verbosity)

    def read(self, key, value, verbosity):
        r = self.session.get(self._path_in_url(key))
        if verbosity:
            print(json.dumps(r.json(), indent=2))            
        if r.status_code != 200:
            raise RuntimeError('Did not succeeds')
        elif verbosity:
            print('suceeds')
        return r.json()['node']['value']

    def do(self, action, key, value, verbosity):
        return {'read': self.read, 'write': self.write, 'delete': self.delete}[action](key, value, verbosity)
