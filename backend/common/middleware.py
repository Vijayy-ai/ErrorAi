import logging
from django.http import JsonResponse
from asgiref.sync import sync_to_async, iscoroutinefunction
import inspect

logger = logging.getLogger(__name__)

class AsyncErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    async def __call__(self, request):
        try:
            response = await self.get_response(request)
            if inspect.isawaitable(response):
                response = await response
            return response
        except Exception as e:
            logger.error(f"Error in request: {str(e)}", exc_info=True)
            return JsonResponse({
                'error': str(e)
            }, status=500)

class AsyncCommonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    async def __call__(self, request):
        response = await self.get_response(request)
        if inspect.isawaitable(response):
            response = await response
        return response 