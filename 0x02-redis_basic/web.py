#!/usr/bin/env python3
"""
 uses the requests module to obtain the HTML content of a
 particular URL and returns it.
"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_connection = redis.Redis()


def data_cache(method: Callable) -> Callable:
    """it caches the output of the fetched data"""

    @wraps(method)
    def wrapper(url) -> str:
        """wrapper function"""
        redis_connection.incr(f"count:{url}")
        output = redis_connection.get(f"output:{url}")
        if output:
            return output.decode('utf-8')
        output = method(url)
        redis_connection.set(f"count:{url}", 0)
        redis_connection.setex(f"output:{url}", 10, output)
        return output
    return wrapper


@data_cache
def get_page(url: str) -> str:
    """returns content of a url after caching"""
    return requests.get(url).text
