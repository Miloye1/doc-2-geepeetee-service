import os

from redis import Redis

password = os.environ.get("KEYDB_PASSWORD")

keydb = Redis(host="localhost", port=6379, decode_responses=True, password=password)
