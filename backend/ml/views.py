from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import AIService
import logging

logger = logging.getLogger(__name__)

class ProcessMessageView(APIView):
    def __init__(self):
        super().__init__()
        self.ai_service = AIService()

    def post(self, request, *args, **kwargs):
        try:
            message = request.data.get('message')
            task_type = request.data.get('task_type')
            
            if not message:
                return Response(
                    {'error': 'Message is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Process synchronously since we're in a sync view
            result = {
                'response': 'Sample response',  # Replace with actual AI processing
                'task_type': task_type or 'conversation'
            }
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) 