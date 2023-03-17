from django.urls import path
from appentrega3.views import inicio, index


urlpatterns = [
    path('', inicio),
    path("index/", index)
]