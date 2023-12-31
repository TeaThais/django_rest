"""
URL configuration for catsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from kitties.views import *
from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'kitties', KittiesViewSet, basename='kitties')    # we use basename when don't use queryset

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/dj-auth/', include('rest_framework.urls')),
    path('api/v1/kitties/', KittiesAPIList.as_view()),
    path('api/v1/kitties/<int:pk>/', KittiesAPIUpdate.as_view()),
    path('api/v1/kittiesdelete/<int:pk>/', KittiesAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/refresh/', TokenVerifyView.as_view(), name='token_refresh'),
    # path('api/v1/', include(router.urls)),    # http://127.0.0.1:8000/api/v1/kitties/   as prefix  r'kitties'
    # path('api/v1/kittieslist/', KittiesViewSet.as_view({'get': 'list'})),
    # path('api/v1/kittieslist/<int:pk>/', KittiesViewSet.as_view({'put': 'update'})),
]