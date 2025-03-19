import time
import functools
from _collections_abc import Callable


def print_runtime(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f"function {func.__name__} took {runtime} seconds")

        return result

    return wrapper
