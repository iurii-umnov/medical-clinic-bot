import json

from pymemcache.client.base import Client
from pymemcache.client.retrying import RetryingClient
from pymemcache.exceptions import MemcacheUnexpectedCloseError

from src.data import config


class JsonSerde(object):
    def serialize(self, key, value):
        if isinstance(value, str):
            return value.encode(config.ENCODING), 1
        return json.dumps(value).encode(config.ENCODING), 2

    def deserialize(self, key, value, flag):
        if flag == 1:
            return value.decode(config.ENCODING)
        if flag == 2:
            return json.loads(value.decode(config.ENCODING))
        raise Exception("Unknown serialization format")


base_cache = Client(
    server=(config.WEBAPPHOST, config.MEMCACHE_PORT),
    serde=JsonSerde()
)
cache = RetryingClient(
    base_cache,
    attempts=2,
    retry_delay=0.01,
    retry_for=[MemcacheUnexpectedCloseError]
)
