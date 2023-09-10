from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
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


class KittiesAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5       # max value for 'page_size' in queries like '&page_size=4'


class KittiesAPIList(generics.ListCreateAPIView):
    queryset = Kitties.objects.all()
    serializer_class = KittiesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = KittiesAPIListPagination


class KittiesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Kitties.objects.all()            # lazy request here returns only one changed object
    serializer_class = KittiesSerializer
    permission_classes = (IsAuthenticated, )


class KittiesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Kitties.objects.all()
    serializer_class = KittiesSerializer
    permission_classes = (IsAdminOrReadOnly, )


