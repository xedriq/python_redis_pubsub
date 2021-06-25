import redis
import time
import os
import json

from multiprocessing import Process

redis_conn = redis.Redis(host=os.getenv('REDIS_HOST', '192.168.3.100'), port=os.getenv(
    'REDIS_PORT', '6379'), charset="utf-8", decode_responses=True)


def sub():
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("broadcast")
    for message in pubsub.listen():
       #  data = json.loads(message.get("data"))
      #   print('do something!!!')
      result = int(message['data']) + 100
      #   time.sleep(1)
      #   print('done!!!')
      f = open("./storage/demofile.txt", "a")
      f.write(str(result)+"\n")
      f.close()


if __name__ == "__main__":
    sub()
    # Process(target=sub, args=("reader1",)).start()
