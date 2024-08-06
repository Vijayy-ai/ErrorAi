# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializer, ChatHistorySerializer
# from .models import ChatHistory
# from services.unified_model import unified_model
# from common.error_handler import error_handler

# class UserRegistrationView(APIView):
#     permission_classes = [AllowAny]

#     @error_handler.handle_error
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLoginView(APIView):
#     permission_classes = [AllowAny]

#     @error_handler.handle_error
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# class ChatbotAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     @error_handler.handle_error
#     async def post(self, request):
#         user_input = request.data.get('message')
#         result = await unified_model.process_input(user_input)
        
#         chat_history = ChatHistory.objects.create(
#             user=request.user,
#             message=user_input,
#             response=result
#         )
        
#         return Response({
#             "chat_id": chat_history.id,
#             "message": user_input,
#             "response": result
#         }, status=status.HTTP_200_OK)

# class ChatHistoryView(APIView):
#     permission_classes = [IsAuthenticated]

#     @error_handler.handle_error
#     def get(self, request):
#         chat_history = ChatHistory.objects.filter(user=request.user)
#         serializer = ChatHistorySerializer(chat_history, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
















#backend/ml/views.py

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, ChatHistorySerializer
from api.models import ChatHistory
from django.contrib.auth.models import User
from services.unified_model import unified_model

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class ChatbotAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_input = request.data.get('message')
        result = unified_model.process_input(user_input)
        
        chat_history = ChatHistory.objects.create(
            user=request.user,
            message=user_input,
            response=result
        )
        
        return Response({
            "chat_id": chat_history.id,
            "message": user_input,
            "response": result
        }, status=status.HTTP_200_OK)

class ChatHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        chat_history = ChatHistory.objects.filter(user=request.user)
        serializer = ChatHistorySerializer(chat_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)