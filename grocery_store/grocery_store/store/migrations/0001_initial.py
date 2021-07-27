# Generated by Django 3.2.5 on 2021-07-27 18:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Bakery', 'Bakery'), ('Fruits', 'Fruits'), ('Vegetables', 'Vegetables'), ('Meat', 'Meat'), ('Rice and Pasta', 'Rice And Pasta'), ('Fish and Seafood', 'Fish and Seafood'), ('Oils, Vinegar and Dried herbs', 'Oils, Vinegar and Dried Herbs'), ('Bear, Wine and Spirits', 'Bear, Wine and Spirits'), ('Soft drinks', 'Soft Drinks'), ('Crisps, Snacks and Nuts', 'Crisps, Snacks and Nuts'), ('Chocolate and Sweets', 'Chocolate and Sweets'), ('unknown', 'Unknown')], default='UNKNOWN', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='price')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
