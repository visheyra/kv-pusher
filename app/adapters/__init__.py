from .etcdV2 import EtcdV2
from .redis import Redis

Adapters = {
    'etcdv2': EtcdV2(),
    'redis': Redis()
}
