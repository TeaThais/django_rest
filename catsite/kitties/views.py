from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Kitties, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import KittiesSerializer


# class KittiesViewSet(viewsets.ModelViewSet):
#    # queryset = Kitties.objects.all()
#     serializer_class = KittiesSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Kitties.objects.all()[:3]
#
#         return Kitties.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})


class KittiesAPIList(generics.ListCreateAPIView):
    queryset = Kitties.objects.all()
    serializer_class = KittiesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class KittiesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Kitties.objects.all()            # lazy request here returns only one changed object
    serializer_class = KittiesSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class KittiesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Kitties.objects.all()
    serializer_class = KittiesSerializer
    permission_classes = (IsAdminOrReadOnly, )


