from django.urls import path
from .views import public_api

urlpatterns = [
    path('', public_api, name='public_api'),
]
