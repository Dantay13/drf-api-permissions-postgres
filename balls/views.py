from rest_framework import generics
from .models import Ball
from .serializers import BallSerializer
from rest_framework.permissions import IsAuthenticated


class BallListCreate(generics.ListCreateAPIView):
    queryset = Ball.objects.all()
    serializer_class = BallSerializer
    permission_classes = [IsAuthenticated]
