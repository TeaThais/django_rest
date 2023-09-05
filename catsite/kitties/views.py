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
        serializer.save()   # method save() calls method CREATE() and adds object

        # new_post = Kitties.objects.create(
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)    # if pk is absent returns None
        if not pk:
            return Response({'error': 'Method PUT is not allowed'})
        # if there is no pk in the url we don't know what to change

        try:
            instance = Kitties.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})    # in case of pk that is not in the table

        serializer = KittiesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()                           # save() calls method UPDATE as we have instance parameter
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE is not allowed'})

        try:
            instance = Kitties.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exist'})
              
        return Response({'post': 'delete post ' + str(pk)})


# class KittiesAPIView(generics.ListAPIView):
#     queryset = Kitties.objects.all()
#     serializer_class = KittiesSerializer
