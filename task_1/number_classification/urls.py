from django.urls import path
from .views import NumberClassificationView

urlpatterns = [
    path('classify-number', NumberClassificationView.as_view(), name='classify-number'),
]