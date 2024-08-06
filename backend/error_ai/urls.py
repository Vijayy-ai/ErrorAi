"""
URL configuration for error_ai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# # backend/error_ai/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Error AI Backend")


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),
#     path('chat/', include('chat.urls')),
#     path('ml/', include('ml.urls')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # Add JWT authentication endpoints
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('', include('django_prometheus.urls')),
#     path('', home), 
    
# ]









# backend/error_ai/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Error AI Backend")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('chat/', include('chat.urls')),
    path('ml/', include('ml.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('django_prometheus.urls')),
    path('', home),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line

]

