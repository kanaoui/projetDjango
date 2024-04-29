# Generated by Django 5.0.4 on 2024-04-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagne', '0003_campagne_fundraiser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campagne',
            name='montant',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='supporteurs',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
