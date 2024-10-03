Here is a list of commonly used **Redis CLI commands** categorized by functionality:

### 1. **Basic Commands**:
- `PING`: Test if Redis is running.
  ```bash
  PING
  ```
- `SET key value`: Set the value of a key.
  ```bash
  SET mykey "Hello"
  ```
- `GET key`: Get the value of a key. (GET is only for string values.)
  ```bash
  GET mykey
  ```
- `DEL key`: Delete a key.
  ```bash
  DEL mykey
  ```

### 2. **Key Management**:
- `EXISTS key`: Check if a key exists.
  ```bash
  EXISTS mykey
  ```
- `EXPIRE key seconds`: Set a timeout on a key.
  ```bash
  EXPIRE mykey 60
  ```
- `TTL key`: Get the remaining time to live of a key.
  ```bash
  TTL mykey
  ```
- `KEYS pattern`: Find all keys matching the given pattern.
  ```bash
  KEYS *
  ```

### 3. **String Commands**:
- `INCR key`: Increment the integer value of a key by 1.
  ```bash
  INCR counter
  ```
- `DECR key`: Decrement the integer value of a key by 1.
  ```bash
  DECR counter
  ```
- `APPEND key value`: Append a value to a key.
  ```bash
  APPEND mykey " World"
  ```
- `MSET key value [key value ...]`: Set multiple keys to multiple values.
  ```bash
  MSET key1 "value1" key2 "value2"
  ```

### 4. **List Commands**:
- `LPUSH key value`: Prepend an element to a list.
  ```bash
  LPUSH mylist "element"
  ```
- `RPUSH key value`: Append an element to a list.
  ```bash
  RPUSH mylist "element"
  ```
- `LPOP key`: Remove and return the first element of a list.
  ```bash
  LPOP mylist
  ```
- `RPOP key`: Remove and return the last element of a list.
  ```bash
  RPOP mylist
  ```
- `LRANGE key start stop`: Get a range of elements from a list.
  ```bash
  LRANGE mylist 0 -1
  ```

### 5. **Set Commands**:
- `SADD key member`: Add one or more members to a set.
  ```bash
  SADD myset "member1"
  ```
- `SMEMBERS key`: Get all members of a set.
  ```bash
  SMEMBERS myset
  ```
- `SPOP key`: Remove and return a random member from a set.
  ```bash
  SPOP myset
  ```

### 6. **Hash Commands**:
- `HSET key field value`: Set the value of a hash field.
  ```bash
  HSET myhash field1 "value1"
  ```
- `HGET key field`: Get the value of a hash field.
  ```bash
  HGET myhash field1
  ```
- `HGETALL key`: Get all fields and values of a hash.
  ```bash
  HGETALL myhash
  ```

### 7. **Sorted Set Commands**:
- `ZADD key score member`: Add a member to a sorted set with a score.
  ```bash
  ZADD myzset 1 "member1"
  ```
- `ZRANGE key start stop [WITHSCORES]`: Get a range of members in a sorted set.
  ```bash
  ZRANGE myzset 0 -1 WITHSCORES
  ```

### 8. **Server Commands**:
- `INFO`: Get information and statistics about the Redis server.
  ```bash
  INFO
  ```
- `FLUSHALL`: Remove all keys from all databases.
  ```bash
  FLUSHALL
  ```
- `DBSIZE`: Return the number of keys in the current database.
  ```bash
  DBSIZE
  ```
- `SAVE`: Save the dataset to disk.<br>
  The file name is dump.rdb (RDB stands for Redis Database).<br>
  On Linux/Unix systems, the default location is usually `/var/lib/redis` or `/etc/redis`.

  ```bash
  SAVE
  ```

### 9. **Transaction Commands**:
- `MULTI`: Mark the start of a transaction block.
  ```bash
  MULTI
  ```
- `EXEC`: Execute all commands issued after `MULTI`.
  ```bash
  EXEC
  ```
- `DISCARD`: Discard the transaction.
  ```bash
  DISCARD
  ```

### 10. **Pub/Sub Commands**:
- `PUBLISH channel message`: Publish a message to a channel.
  ```bash
  PUBLISH mychannel "Hello, world!"
  ```
- `SUBSCRIBE channel`: Subscribe to a channel.
  ```bash
  SUBSCRIBE mychannel
  ```

### 11. **Persistence and Backup**:
- `BGSAVE`: Save data to disk asynchronously in the background.
  ```bash
  BGSAVE
  ```
- `LASTSAVE`: Get the Unix timestamp of the last successful `SAVE` operation.
  ```bash
  LASTSAVE
  ```

For a **complete list of Redis commands** and more details, you can refer to the official Redis documentation here:
[Redis Documentation](https://redis.io/commands/)