
# # backend/utils/error_handler.py
# import logging
# from django.conf import settings
# from functools import wraps
# import asyncio
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
#                 if settings.DEBUG:
#                     return f"An error occurred: {str(e)}"
#                 else:
#                     return "An unexpected error occurred. Please try again later."
#         return wrapper

# error_handler = ErrorHandler()






import logging
from functools import wraps
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class ErrorHandler:
    @staticmethod
    def handle_error(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return wrapper

error_handler = ErrorHandler()
