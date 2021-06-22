import redis
import time

from multiprocessing import Process

redis_conn = redis.Redis(host='localhost', port='6377', charset="utf-8", decode_responses=True)

def sub(name: str):
   pubsub = redis_conn.pubsub()
   pubsub.subscribe("broadcast")
   for message in pubsub.listen():
    #    data = json.loads(message.get("data"))
       print(message.get('data'))
       print('do something!!!')
       time.sleep(10)
       print('done!!!')


if __name__ == "__main__":
   Process(target=sub, args=("reader1",)).start()