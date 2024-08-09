

from .views import ChatbotAPIView
# # backend/api/urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView, ChatbotAPIView, ChatHistoryView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
    path('chat-history/', ChatHistoryView.as_view(), name='chat_history'),
    
]