from concurrent import futures
from datetime import datetime
import functools
import time


def timer(func):

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

        print(f'START {func.__name__!r} at {datetime.now()}')
        value = func(*args, **kwargs)
        print(f'FINISH {func.__name__!r} at {datetime.now()}')

        run_time = time.perf_counter() - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')

        return value
    return wrapper_timer


def execute_in_threads(max_threads: int, urls_per_thread: int):

    def decorator_fun(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Extract list of URLs from arguments
            list_of_urls = kwargs['cat_urls']
            urls_for_threads = list()

            # Split list of string URLs into list of smaller lists
            # Each small list contains `urls_per_thread` URLs
            for i in range(0, len(list_of_urls), urls_per_thread):
                urls_for_threads.append(list_of_urls[i:i+urls_per_thread])

            # Run function in multiple threads
            # For each thread a small list with `urls_per_thread` URLs passed
            with futures.ThreadPoolExecutor(max_workers=max_threads) as ex:
                ex.map(func, urls_for_threads)

        return wrapper

    return decorator_fun
