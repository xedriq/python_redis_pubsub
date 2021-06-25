FROM python:3.9

RUN pip install --upgrade pip

RUN pip install redis

WORKDIR /app

ENV REDIS_HOST='192.168.3.100'

ENV REDIS_PORT="6379"

COPY sub.py .

# ENTRYPOINT [ "python" ]
CMD [ "python", "sub.py" ]