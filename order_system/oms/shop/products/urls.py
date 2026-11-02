from django.http import HttpResponse
from django.urls import path

app_name = "products"

urlpatterns = [
    path(
        "",
        lambda request: HttpResponse("Products app OK - LDW"),
        name="index",
    ),
]