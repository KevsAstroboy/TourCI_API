# Generated by Django 4.2.2 on 2023-06-26 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_sitetouristique_ville'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stade',
            old_name='description_site',
            new_name='description_stade',
        ),
        migrations.RenameField(
            model_name='stade',
            old_name='nom_site',
            new_name='nom_stade',
        ),
    ]