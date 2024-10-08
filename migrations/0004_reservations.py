# Generated by Django 4.2.14 on 2024-08-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pav', '0003_alter_portfolioexperts_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=500)),
                ('email', models.EmailField(default=True, max_length=254)),
                ('password', models.FloatField(default=False)),
                ('re_password', models.FloatField(default=False)),
                ('adresse', models.FloatField(default=True)),
            ],
        ),
    ]
