from core.models import *


def get_count(request):
    count_provider = Provider.objects.count()
    count_client = Client.objects.count()
    count_produit = Produit.objects.count()
    count_vehicule = Vehicule.objects.count()
    count_commande = Commande.objects.count()

    return locals()