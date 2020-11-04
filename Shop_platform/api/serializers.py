from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer
from rest_framework import serializers
from shops.models import Shop, Product

class ShopSerializer(HyperlinkedModelSerializer):

    owner = serializers.CharField(read_only=True, source="owner.user")
    url = HyperlinkedIdentityField(view_name="shops-api:shop-detail", lookup_field="slug")
    #products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Shop
        fields = ["url", 'name', 'id', 'owner']
        

"""
class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["name", "date", "seller", "price", "category"]

"""
