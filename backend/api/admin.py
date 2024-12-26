from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'task_type', 'created_at')
    list_filter = ('task_type', 'created_at')
    search_fields = ('message', 'response')
    ordering = ('-created_at',)