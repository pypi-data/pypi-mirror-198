import time
import sys
import datetime
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = (time.time() - start_time) * 1000
        print(f"{elapsed_time:.3f} ms")
        return result
    return wrapper

def timejob(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        dt = (end-start) * 1000
        caller = sys._getframe(1)
        my_time = '{0:%H:%M:%S:%f}'.format(datetime.datetime.now())
        print(">[{}] [{:.3f}ms] [{}] [{}]".format(my_time, dt, func.__name__, caller.f_globals['__name__']))
        return r
    return wrapper