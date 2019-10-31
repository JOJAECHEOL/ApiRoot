from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Post', views.PostViewSet)

router.register('PostPic', views.PostPicViewSet)

router.register('PostFile', views.PostFileViewSet)


urlpatterns = [
    path('',include(router.urls)),
]