# Generated by Django 3.1.2 on 2020-11-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0002_auto_20201125_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='v_item',
            name='my_image',
        ),
        migrations.AddField(
            model_name='v_item',
            name='my_file',
            field=models.FileField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
