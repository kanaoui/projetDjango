# Generated by Django 5.0.4 on 2024-04-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_number', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('nom', models.CharField(max_length=100)),
                ('histoire', models.TextField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=6)),
                ('supporteurs', models.CharField(max_length=100)),
            ],
        ),
    ]
