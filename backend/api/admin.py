# 
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import MongoUser, ChatHistory

# class MongoUserAdmin(UserAdmin):
#     model = MongoUser
#     list_display = ('username', 'email', 'is_staff', 'is_active',)
#     list_filter = ('is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('username', 'email',)
#     ordering = ('username',)

# admin.site.register(MongoUser, MongoUserAdmin)
# admin.site.register(ChatHistory)

# File: backend/api/admin.py
from django.contrib import admin
from .models import ChatHistory

admin.site.register(ChatHistory)