# python package to intract with redis ( https://pypi.org/project/redis/ )
# pip install redis


# Basic Example
# >>> import redis
# >>> r = redis.Redis(host='localhost', port=6379, db=0)
# >>> r.set('foo', 'bar')
# True
# >>> r.get('foo')
# b'bar'

import redis
import redis.asyncio as redis_asyncio


r = redis.Redis(host='localhost', port=6379, db=0)