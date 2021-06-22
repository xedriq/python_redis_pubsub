import os
import redis
import json

from multiprocessing import Process

redis_conn = redis.Redis(charset="utf-8", decode_responses=True)

def sub(name: str):
   pubsub = redis_conn.pubsub()
   pubsub.subscribe("broadcast")
   for message in pubsub.listen():
    #    data = json.loads(message.get("data"))
       print(message.get('data'))
       print('do something!!!')


if __name__ == "__main__":
   Process(target=sub, args=("reader1",)).start()