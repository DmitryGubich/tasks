import asyncio
from functools import wraps
from time import time


def time_it(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(f"Took {total_time:.2f} seconds")
        return result

    return timeit_wrapper


async def f():
    await asyncio.sleep(1)
    return 2


async def g():
    await asyncio.sleep(3)
    return 3


async def h():
    await asyncio.sleep(2)
    return 1


@time_it
def find_max_in_async():
    tasks = [f(), g(), h()]
    loop = asyncio.get_event_loop()
    return max(loop.run_until_complete(asyncio.gather(*tasks)))


if __name__ == "__main__":
    assert find_max_in_async() == 3
