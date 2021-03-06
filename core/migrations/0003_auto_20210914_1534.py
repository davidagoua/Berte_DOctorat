# Generated by Django 3.2.7 on 2021-09-14 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210914_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produit'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='quantite',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='depots',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='provider',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='capacitecompat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='cout',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='nombrecompat',
            field=models.IntegerField(),
        ),
    ]
