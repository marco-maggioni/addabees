"""addabees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bees import views as bees_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bees_views.homepage, name="home"),
    path('chi_siamo/', bees_views.chi_siamo, name="chi_siamo"),
    path('contatti/', bees_views.contatti, name="contatti"),
    path('il_miele/', bees_views.il_miele, name="il_miele"),
    path('gallery/', bees_views.gallery, name="gallery")
]
