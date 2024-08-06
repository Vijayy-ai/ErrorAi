# # backend/ml/views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from services import unified_model
# from common import error_handler
# from rest_framework import status

# class ProcessMLView(APIView):
#     @error_handler.handle_error
#     async def post(self, request):
#         user_input = request.data.get('input')
#         result = await unified_model.process_input(user_input)
#         return Response({'result': result}, status=status.HTTP_200_OK)

#     @error_handler.handle_error
#     async def get(self, request):
#         return Response({'message': 'Use POST to process ML requests'}, status=status.HTTP_200_OK)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.error_handler import error_handler
from services import unified_model

class ProcessMLView(APIView):
    @error_handler.handle_error
    async def post(self, request):
        user_input = request.data.get('input')
        result = await unified_model.process_input(user_input)
        return Response({'result': result}, status=status.HTTP_200_OK)

    @error_handler.handle_error
    async def get(self, request):
        return Response({'message': 'Use POST to process ML requests'}, status=status.HTTP_200_OK)
