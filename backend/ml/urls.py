from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.ProcessMessageView.as_view(), name='process_message'),
] 