import redis

r = redis.Redis(
  host='redis-15051.c292.ap-southeast-1-1.ec2.cloud.redislabs.com',
  port=15051,
  password='Ymb9U2OmeJ3czx5eG6XFZ9WH7rTOoMOB')

print(r.ping())