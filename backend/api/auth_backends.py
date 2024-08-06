# # backend/api/auth_backends.py

# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.hashers import check_password
# from .mongo_models import User

# class MongoAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = User.get_by_username(username)
#             if user and check_password(password, user['password']):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.get_by_id(user_id)
#         except User.DoesNotExist:
#             return None