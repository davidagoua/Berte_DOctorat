from django.contrib import admin
from .models import *


@admin.register(Provider, Depots, Client)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['nom','code','type','x','y']


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ['nom','nombrecompat','capacitecompat','cout']


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom','code','provider']


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['quantite','provider','produit']
