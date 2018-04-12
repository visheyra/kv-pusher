import redis

class Redis:

    def __init__(self):
        pass

    def configure(self, endpoint, port):
        self.endpoint = endpoint
        self.port = port
        self.cli = redis.StrictRedis(host=self.endpoint, port=self.port)

    def write(self, key, value, verbosity=False):
        self.cli.set(key, value)
        if verbosity:
            print('key [{}] written'.format(key))

    def delete(self, key, value, verbosity=False):
        self.cli.delete(key)
        if verbosity:
            print('key [{}] written'.format(key))

    def update(self, key, value, verbosity=False):
        self.write(key, value, verbosity)

    def read(self, key, value, verbosity=False) -> str:
        ret = self.cli.get(key)
        if verbosity:
            print('key [{}] read'.format(key))
        return ret.decode('utf-8')

    def do(self, action, key, value, verbosity):
        return {'read': self.read, 'write': self.write, 'delete': self.delete}[action](key, value, verbosity)
