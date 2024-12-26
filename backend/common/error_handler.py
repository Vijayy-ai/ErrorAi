from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def error_handler(error):
    """
    Simple error handler for non-DRF contexts
    """
    error_message = str(error)
    return {
        'error': error_message,
        'status': status.HTTP_400_BAD_REQUEST
    }

def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF views
    """
    response = exception_handler(exc, context)

    if response is None:
        response = Response({
            'error': str(exc),
            'detail': 'An unexpected error occurred'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response 