#backend/api/models.py
from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    TASK_TYPES = [
        ('code_generation', 'Code Generation'),
        ('code_explanation', 'Code Explanation'),
        ('error_fixing', 'Error Fixing'),
        ('conversation', 'Conversation'),
    ]
    
    message = models.TextField()
    response = models.TextField()
    task_type = models.CharField(max_length=50, choices=TASK_TYPES, default='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'api'
        db_table = 'api_chatmessage'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['task_type']),
        ]

    def __str__(self):
        return f"{self.task_type} - {self.created_at}"