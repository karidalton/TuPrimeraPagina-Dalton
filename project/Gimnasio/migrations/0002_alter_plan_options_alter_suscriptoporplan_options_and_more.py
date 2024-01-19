# Generated by Django 5.0.1 on 2024-01-18 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gimnasio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'plan', 'verbose_name_plural': 'Planes'},
        ),
        migrations.AlterModelOptions(
            name='suscriptoporplan',
            options={'verbose_name': 'suscriptor por plan', 'verbose_name_plural': 'suscriptores por plan'},
        ),
        migrations.AlterModelOptions(
            name='suscriptoporsede',
            options={'verbose_name': 'suscriptor por sede', 'verbose_name_plural': 'sucriptores por sede'},
        ),
        migrations.AlterModelOptions(
            name='suscriptor',
            options={'verbose_name': 'suscriptor', 'verbose_name_plural': 'sucriptores'},
        ),
        migrations.RemoveField(
            model_name='suscriptor',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='suscriptor',
            name='sede',
        ),
    ]
