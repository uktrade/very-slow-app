import time
import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def sleep_endpoint():
    time.sleep(10)
    return 'OK'


def slow_func(size=1000):
    sorted(map(lambda x: random.normalvariate(5, 5), range(size*1000)))


@app.route('/compute')
def compute_endpoint():
    """
    View that actively utilizes one CPU core for 10s
    :return:
    """
    wait_for_seconds = 10
    now_time = start_time = time.time()
    while now_time - start_time < wait_for_seconds:
        slow_func()
        now_time = time.time()
        print(now_time - start_time)
    return 'OK'

