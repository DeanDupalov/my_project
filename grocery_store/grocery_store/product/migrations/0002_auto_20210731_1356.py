# Generated by Django 3.2.5 on 2021-07-31 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountproduct',
            name='id',
        ),
        migrations.AlterField(
            model_name='discountproduct',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='product.product'),
        ),
    ]