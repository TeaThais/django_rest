from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Kitties
from .serializers import KittiesSerializer


class KittiesAPIView(APIView):
    def get(self, request):
        lst = Kitties.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        new_post = Kitties.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(new_post)})


# class KittiesAPIView(generics.ListAPIView):
#     queryset = Kitties.objects.all()
#     serializer_class = KittiesSerializer
