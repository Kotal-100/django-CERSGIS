from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("Services/", include("Services.urls")),
    
]