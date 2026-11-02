from django.urls import path, include
from .views import HomePageView

app_name = "shop"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("products/", include(("shop.products.urls", "products"), namespace="products"))
]