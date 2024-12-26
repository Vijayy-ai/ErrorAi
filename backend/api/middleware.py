from channels.middleware import BaseMiddleware
from django.core.cache import cache
import time

class WebSocketRateLimitMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Get client IP
        client_ip = scope.get('client')[0]
        
        # Check rate limit (100 requests per hour)
        cache_key = f"ws_ratelimit_{client_ip}"
        request_count = cache.get(cache_key, 0)
        
        if request_count >= 100:
            # Rate limit exceeded
            await send({
                "type": "websocket.close",
                "code": 4429  # Custom code for rate limit
            })
            return
            
        # Increment request count
        cache.set(cache_key, request_count + 1, timeout=3600)  # 1 hour expiry
        
        return await super().__call__(scope, receive, send) 