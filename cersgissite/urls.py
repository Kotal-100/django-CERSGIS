"""
URL configuration for cersgissite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Contactus import views




urlpatterns = [
     path("About-us/", include("Aboutus.urls")),
     path("Blog/", include("Blog.urls")),
     path("Galler/", include("Gallery.urls")),
     path("", include("Home.urls")),
     path("Maps", include("Maps.urls")),
     path("Products/", include("Products.urls")),
    #  path("Contactus/", include("Contactus.urls")),
     path("Services/", include("Services.urls")),
     path('contact-us/', views.Contactus, name='Contactus'),
     path('admin/', admin.site.urls),
]

 