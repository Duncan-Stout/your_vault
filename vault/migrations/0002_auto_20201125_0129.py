# Generated by Django 3.1.2 on 2020-11-25 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vault_shelf',
            new_name='V_item',
        ),
    ]
