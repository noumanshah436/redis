# python package to intract with redis ( https://pypi.org/project/redis/ )
# pip install redis

# The redis Python package provides a simple interface to interact with a Redis database.

# *******************************************

# Basic Example
# >>> import redis
# >>> r = redis.Redis(host='localhost', port=6379, db=0)
# >>> r.set('foo', 'bar')
# True
# >>> r.get('foo')
# b'bar'

# *******************************************


import redis
import redis.asyncio as redis_asyncio


r = redis.Redis(host='localhost', port=6379, db=0)
r.set('key', 'value')
r.set('user_name', 'Nouman')

print(r.get('key'))

# delete redis entry
r.delete('key')
r.delete('user_name')

# Set the key to expire in 20 seconds
r.expire('key', 20)

# *******************************************


# Redis `set` Method
# The `set` method stores a key-value pair in the Redis database. In addition to just setting a value, you can use several optional parameters:

# ```python
# r.set(name, value, ex=None, px=None, nx=False, xx=False, keepttl=False, get=False)
# ```

# ### Key Arguments for `set` Method

# - **`ex`**: Expiration time in **seconds**.
#   - Example: `r.set('foo', 'bar', ex=10)` will set the key to expire in 10 seconds.

# - **`px`**: Expiration time in **milliseconds**.
#   - Example: `r.set('foo', 'bar', px=5000)` will set the key to expire in 5,000 milliseconds (5 seconds).

# - **`nx`**: Set the value **only if the key does not already exist**.
#   - Example: `r.set('foo', 'bar', nx=True)` will only set the key if it doesn’t already exist.

# - **`xx`**: Set the value **only if the key already exists**.
#   - Example: `r.set('foo', 'bar', xx=True)` will only set the key if it already exists.

# - **`keepttl`**: Retains the TTL (time-to-live) of the key if it already has one.
#   - Example: `r.set('foo', 'bar', keepttl=True)` will retain the original expiration time of the key if it exists.

# - **`get`**: Returns the old value of the key if it existed.
#   - Example: `r.set('foo', 'new_value', get=True)` will return the old value (if it existed) and set the new value.

# ### Example Usage of `set` with Arguments

# ```python
# # Set with expiration of 10 seconds and only if the key doesn't exist
# r.set('foo', 'bar', ex=10, nx=True)
# ```

# *******************************************

# Redis `expire` Method

# The `expire` method is used to set a timeout on a key that already exists in Redis.
# Once the timeout has expired, the key will automatically be deleted.

# ```python
# r.expire(name, time)
# ```

# - **`name`**: The key you want to set an expiration for.
# - **`time`**: The expiration time. It can be specified as:
#   - An integer (number of **seconds**).
#   - A `timedelta` object from Python's `datetime` module.

### Example Usage of `expire`

# ```python
# # Set a key without expiration
# r.set('foo', 'bar')

# # Set the key to expire in 20 seconds
# r.expire('foo', 20)

# # Alternatively, using timedelta for expiration
# from datetime import timedelta
# r.expire('foo', timedelta(minutes=1))  # Expires in 1 minute
# ```

# *******************************************
