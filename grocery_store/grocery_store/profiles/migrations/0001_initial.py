# Generated by Django 3.2.5 on 2021-07-23 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('grocery_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='grocery_auth.groceryuser')),
                ('products', models.ManyToManyField(blank=True, to='store.Product')),
            ],
        ),
    ]
