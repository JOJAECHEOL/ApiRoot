from django.shortcuts import render
from .models import Post,PostPic,PostFile
from .serializer import PostSerializer,PostPicSerializer,PostFileSerializer

from rest_framework import viewsets

from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('id')   
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()  

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

class PostPicViewSet(viewsets.ModelViewSet):

    queryset = PostPic.objects.all().order_by('id')
    serializer_class = PostPicSerializer


class PostFileViewSet(viewsets.ModelViewSet):

    queryset = PostFile.objects.all().order_by('id')    
    serializer_class = PostFileSerializer

class Mypagination(PageNumberPagination):
    page_size = 100