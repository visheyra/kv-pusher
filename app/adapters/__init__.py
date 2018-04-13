from .etcdV2 import EtcdV2
from .redis import Redis
from .consul import Consul

Adapters = {
    'etcdv2': EtcdV2(),
    'redis': Redis(),
    'consul': Consul()
}
