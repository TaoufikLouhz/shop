# Generated by Django 4.2 on 2023-05-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]
