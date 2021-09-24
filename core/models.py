from django.db import models


class BaseClass(models.Model):
    nom = models.CharField(max_length=50)
    type = models.IntegerField(default=0)
    code = models.CharField(max_length=21)
    x = models.DateTimeField()
    y = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

    def __str__(self): return self.nom


class Provider(BaseClass):
    pass


class Depots(BaseClass):
    pass


class Vehicule(BaseClass):
    x = None
    y = None
    type = None
    nombrecompat = models.IntegerField()
    capacitecompat = models.IntegerField()
    cout = models.PositiveIntegerField()


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): return self.nom

class Client(BaseClass):
    pass



class Commande(models.Model):
    quantite = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): return self.pk



