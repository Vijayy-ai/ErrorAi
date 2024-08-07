
# # backend/utils/cache.py
import asyncio
from collections import OrderedDict

class AsyncCache:
    def __init__(self, max_size=100):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.lock = asyncio.Lock()

    async def get(self, key):
        async with self.lock:
            if key in self.cache:
                value = self.cache.pop(key)
                self.cache[key] = value
                return value
        return None

    async def set(self, key, value):
        async with self.lock:
            if key in self.cache:
                self.cache.pop(key)
            elif len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
            self.cache[key] = value

response_cache = AsyncCache()








# from django.core.cache import cache

# class ResponseCache:
#     @staticmethod
#     def get(key):
#         return cache.get(key)

#     @staticmethod
#     def set(key, value, timeout=3600):  # Cache for 1 hour by default
#         cache.set(key, value, timeout)

# response_cache = ResponseCache()