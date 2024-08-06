
# # backend/utils/cache.py

# from django.core.cache import cache

# class ResponseCache:
#     @staticmethod
#     def get(key):
#         return cache.get(key)

#     @staticmethod
#     def set(key, value, timeout=3600):  # Cache for 1 hour by default
#         cache.set(key, value, timeout)

# response_cache = ResponseCache()



from django.core.cache import cache

class ResponseCache:
    @staticmethod
    def get(key):
        return cache.get(key)

    @staticmethod
    def set(key, value, timeout=3600):  # Cache for 1 hour by default
        cache.set(key, value, timeout)

response_cache = ResponseCache()