# Generated by Django 2.2.1 on 2019-05-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_film_linkimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='linkImg',
        ),
    ]
