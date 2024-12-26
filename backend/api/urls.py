from django.urls import path
from . import views

urlpatterns = [
    path('chat-history/', views.ChatHistoryView.as_view(), name='chat_history'),
    path('chatbot/', views.ChatbotView.as_view(), name='chatbot'),
]