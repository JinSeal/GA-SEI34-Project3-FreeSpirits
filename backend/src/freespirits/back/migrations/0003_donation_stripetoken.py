# Generated by Django 3.0 on 2019-12-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_auto_20191217_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='stripetoken',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]