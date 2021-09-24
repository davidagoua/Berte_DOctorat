from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.views import generic


def index(request):
    providers = Provider.objects.all()
    clients = Client.objects.all()
    produits = Produit.objects.all()
    return render(request, 'index2.html', locals())


def add_provider(request):
    if request.method == 'POST':
        Provider.objects.create(
            nom= request.POST.get('nom',None),
            type= request.POST.get('type',None),
            code= request.POST.get('code',None),
            x= request.POST.get('x',None),
            y= request.POST.get('y',None),
        )
        messages.success(request, "Fournisseur Enregistré")

    return redirect('list_provider')


def add_produit(request):
    if request.method == 'POST':
        Produit.objects.create(
            nom=request.POST.get('nom', None),
            code=request.POST.get('code', None),
            provider_id=request.POST.get('provider_id', None),
        )
        messages.success(request, "produit Enregistré")
    return redirect('list_produit')


def add_client(request):
    if request .method == 'POST':
        Client.objects.create(
            nom=request.POST.get('nom',None),
            type=request.POST.get('type',None),
            code=request.POST.get('code',None),
            x=request.POST.get('x',None),
            y=request.POST.get('y',None),
        )
        messages.success(request, "Client Enrégistré")
    return redirect('list_client')


def add_vehicule(request):
    if request.method == 'POST':
        Vehicule.objects.create(
            nom=request.POST.get('nom', None),
            nombrecompat=request.POST.get('nombrecompat', None),
            capacitecompat=request.POST.get('capacitecompat', None),
            cout=request.POST.get('cout', None),
        )
        messages.success(request, "Vehicule ajouté")
    return redirect('list_vehicule')


def add_commande(request):
    if request.method == 'POST':
        Commande.objects.create(
            quantite=request.POST.get('quantite', None),
            client= get_object_or_404(Client, pk=request.POST.get('client_id',None)),
            produit= get_object_or_404(Produit, pk=request.POST.get('produit_id',None)),
            provider= get_object_or_404(Provider, pk=request.POST.get('provider_id',None)),
        )
        messages.success(request, "Commande ajouté")
    return redirect('list_commande')


def list_provider(request):
    providers = Provider.objects.all()
    return render(request, 'list_provider.html', locals())


def list_produit(request):
    providers = Provider.objects.all()
    produits = Produit.objects.select_related('provider').all()
    return render(request, 'list_produit.html', locals())


def list_client(request):
    clients = Client.objects.all()
    return render(request, 'list_client.html', locals())


def list_vehicule(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'list_vehicule.html', locals())


def list_commande(request):
    clients = Client.objects.all()
    providers = Provider.objects.all()
    produits = Produit.objects.select_related('provider').all()
    commandes = Commande.objects.select_related('provider','produit','client').all()
    print(clients)
    return render(request, 'list_command.html', locals())