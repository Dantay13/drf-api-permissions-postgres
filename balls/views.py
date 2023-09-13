from rest_framework import generics
from .models import Ball
from .serializers import BallSerializer


class BallListCreate(generics.ListCreateAPIView):
    queryset = Ball.objects.all()
    serializer_class = BallSerializer
