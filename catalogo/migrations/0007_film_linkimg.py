# Generated by Django 2.2.1 on 2019-05-22 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_film_cartel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='linkImg',
            field=models.URLField(blank=True, null=True),
        ),
    ]
