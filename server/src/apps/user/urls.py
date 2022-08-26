from django.urls import path
from src.apps.user.views import saludo

urlpatterns = [
    path("", saludo)
]
