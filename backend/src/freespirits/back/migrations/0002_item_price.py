# Generated by Django 3.0 on 2019-12-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
