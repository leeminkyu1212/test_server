from django.shortcuts import render

# Create your views here

from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
