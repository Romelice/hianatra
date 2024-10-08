# Generated by Django 4.2.14 on 2024-08-15 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pav', '0002_portfolioexperts_portfolioproduit_portfolioservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioexperts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='experts'),
        ),
        migrations.AlterField(
            model_name='portfolioproduit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produits'),
        ),
        migrations.AlterField(
            model_name='portfolioservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services'),
        ),
    ]
