# Generated by Django 2.0.9 on 2018-12-13 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0002_auto_20181213_1700'),
        ('leis', '0012_artigo_is_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lei',
            name='pacote',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='lei', to='pacotes.Pacote', verbose_name='Pacote'),
        ),
    ]
