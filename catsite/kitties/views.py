from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Kitties
from .serializers import KittiesSerializer


class KittiesAPIView(APIView):
    def get(self, request):
        lst = Kitties.objects.all()
        return Response({'posts': KittiesSerializer(lst, many=True).data})       # many=True because of list

    def post(self, request):
        serializer = KittiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # to get exception as JSON string

        new_post = Kitties.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': KittiesSerializer(new_post).data})


# class KittiesAPIView(generics.ListAPIView):
#     queryset = Kitties.objects.all()
#     serializer_class = KittiesSerializer
