from rest_framework import serializers
from .models import Post,PostPic,PostFile


class PostSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')

    class Meta:
        model=Post
        fields=('pk','title','body','author')

class PostPicSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    myimage = serializers.ImageField(use_url=True)

    class Meta:
        model = PostPic
        fields = ('pk', 'author', 'myimage','desc')    # 여기서 fields를 해주기 위해서 우리가 위에서 declare를 해줘야한다


class PostFileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True) 

    class Meta:
        model = PostFile
        fields = ('pk', 'author', 'myfile', 'desc')   