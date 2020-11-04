from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.models import Profile
from .serializers import ShopSerializer
from rest_framework.response import Response
from shops.models import Shop, Product
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ShopViewSet(ModelViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)