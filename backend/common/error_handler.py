#backend/common/error_handler.py
import functools
import logging
from asgiref.sync import iscoroutinefunction, async_to_sync
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class ErrorHandler:
    @staticmethod
    def handle_error(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if iscoroutinefunction(func):
                    return async_to_sync(func)(*args, **kwargs)
                else:
                    return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return wrapper

error_handler = ErrorHandler()












# import logging
# from functools import wraps
# from rest_framework.response import Response
# from rest_framework import status

# logger = logging.getLogger(__name__)

# class ErrorHandler:
#     @staticmethod
#     def handle_error(func):
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#             try:
#                 return await func(*args, **kwargs)
#             except Exception as e:
#                 logger.error(f"Error in {func.__name__}: {str(e)}")
#                 return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return wrapper

# error_handler = ErrorHandler()
