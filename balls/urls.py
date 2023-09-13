from django.urls import path
from .views import BallListCreate

urlpatterns = [
    path('balls/', BallListCreate.as_view(), name='ball-list-create'),
]
