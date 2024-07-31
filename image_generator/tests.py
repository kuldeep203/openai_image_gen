import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve all keys
keys = r.keys('*')

# Print data for each key
for key in keys:
    key_type = r.type(key).decode('utf-8')
    print(f'Key: {key.decode("utf-8")}, Type: {key_type}')

    if key_type == 'string':
        print(f'Value: {r.get(key).decode("utf-8")}')
    elif key_type == 'list':
        print(f'Values: {r.lrange(key, 0, -1)}')
    elif key_type == 'set':
        print(f'Values: {r.smembers(key)}')
    elif key_type == 'hash':
        print(f'Values: {r.hgetall(key)}')
    elif key_type == 'zset':
        print(f'Values: {r.zrange(key, 0, -1, withscores=True)}')
    else:
        print('Unsupported key type')
