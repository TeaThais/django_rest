from django.shortcuts import render
from rest_framework import generics
from .models import Kitties
from .serializers import KittiesSerializer


class KittiesAPIView(generics.ListAPIView):
    queryset = Kitties.objects.all()
    serializer_class = KittiesSerializer
