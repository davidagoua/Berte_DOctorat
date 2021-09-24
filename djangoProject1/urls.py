"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from core.controllers.CommandController import CommandController
from core.views import *

urlpatterns = [

    # create
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('provider/add/', add_provider, name='add_provider'),
    path('produit/add/', add_produit, name='add_produit'),
    path('client/add/', add_client, name='add_client'),
    path('vehicule/add/', add_vehicule, name='add_vehicule'),
    path('commande/add/', add_commande, name='add_commande'),

    # list
    path('providers/', list_provider, name='list_provider'),
    path('produits/', list_produit, name='list_produit'),
    path('clients/', list_client, name='list_client'),
    path('vehicules/', list_vehicule, name='list_vehicule'),
    path('commandes/', list_commande, name='list_commande')

]
