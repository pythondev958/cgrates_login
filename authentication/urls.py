from django.urls import path
from .api import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]