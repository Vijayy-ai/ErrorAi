# backend/chat/models.py
from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_chathistory_set')
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    @classmethod
    def get_by_user(cls, user_id):
        return cls.objects.filter(user__id=user_id)

        
        
# #backend/chat/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class ChatHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_chathistory_set')
#     # other fields...
#     message = models.TextField()
#     response = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-timestamp']
        
        