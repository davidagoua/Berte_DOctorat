from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from core.models import *


class CommandController(object):

    @staticmethod
    def add_commande(request):
        if request.method == 'POST':
            Commande.objects.create(
                quantite=request.POST.get('quantite', None),
                client=get_object_or_404(Client, pk=request.POST.get('client_id', None)),
                produit=get_object_or_404(Produit, pk=request.POST.get('produit_id', None)),
                provider=get_object_or_404(Provider, pk=request.POST.get('provider_id', None)),
            )
            messages.success(request, "Commande ajouté")
        return redirect('index')

    @staticmethod
    def list_commande(request):
        commandes = Commande.objects.select_related('provider', 'produit', 'client').all()
        return render(request, 'list_command.html', locals())