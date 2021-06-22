import os
import redis
import json

redis_conn = redis.Redis(host='localhost', port='6377', charset="utf-8", decode_responses=True)

def pub():
    for i in range(20):
        data = {
            "message": i,
        }
        redis_conn.publish("broadcast", json.dumps(data))

if __name__ == "__main__":
    pub()