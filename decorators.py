import datetime
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"Execution time of {func.__name__}: {end_time - start_time}")
        return result
    return wrapper


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Method {func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
