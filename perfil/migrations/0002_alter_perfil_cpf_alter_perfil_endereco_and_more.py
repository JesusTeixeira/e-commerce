# Generated by Django 4.0.5 on 2022-06-05 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
