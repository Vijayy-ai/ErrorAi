# # backend/chat/views.py
# from django.shortcuts import render
# from django.views import View
# from chat.models import ChatHistory


# class ChatbotView(View):
#     def get(self, request):
#         user_id = request.user.id
#         chat_history = ChatHistory.get_by_user(user_id)
#         return render(request, 'chat/chatbot.html', {'chat_history': chat_history})

# backend/chat/views.py
from django.shortcuts import render
from django.views import View
from .models import ChatHistory
from django.contrib.auth.mixins import LoginRequiredMixin

class ChatbotView(LoginRequiredMixin, View):
    def get(self, request):
        chat_history = ChatHistory.objects.filter(user=request.user)
        return render(request, 'chat/chatbot.html', {'chat_history': chat_history})


# # backend/chat/views.py
# from .models import ChatHistory
# from django.shortcuts import render
# from django.views import View
# from api.models import ChatHistory

# class ChatbotView(View):
#     async def get(self, request):
#         chat_history = await ChatHistory.get_by_user(str(request.user.id))
#         return render(request, 'chat/chatbot.html', {'chat_history': chat_history})