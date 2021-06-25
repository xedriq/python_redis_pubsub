import os
import redis
import json
import time

redis_conn = redis.Redis(host=os.getenv('REDIS_HOST', '192.168.3.100'), port=os.getenv('REDIS_PORT','6379'), charset="utf-8", decode_responses=True)

def pub():
    for i in range(100):
        
        redis_conn.publish("broadcast", i)

if __name__ == "__main__":
    pub()