from rest_framework.routers import DefaultRouter 
from .views import ShopViewSet
from shops.models import Shop
from .serializers import ShopSerializer
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

router = DefaultRouter()

router.register("Shops", ShopViewSet, basename="shop")
#router.register("products", ProductViewSet)

shop_list = ShopViewSet.as_view({"get":"list", "post":"create"})
shop_detail = ShopViewSet.as_view({"get":"retrieve"})

urlpatterns = [

    path("shops/", shop_list, name="shop-list"),
    path("shops/<slug:slug>/", shop_detail, name="shop-detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json"])
