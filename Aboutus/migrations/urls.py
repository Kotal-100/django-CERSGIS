from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("Aboutus/", include("Aboutus.urls")),
    
]