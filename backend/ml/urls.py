#backend/ml/urls.py
from django.urls import path
from .views import ProcessMLView

urlpatterns = [
    path('process/', ProcessMLView.as_view(), name='process_ml'),
]