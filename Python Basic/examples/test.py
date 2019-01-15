from rq import Queue
from redis import Redis
from my_module import count_words_at_url
import time

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue_call(func=count_words_at_url,
               args=('http://nvie.com',),
               timeout=5)
print(job.result)   # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)   # => 889
