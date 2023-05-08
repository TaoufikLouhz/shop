# Generated by Django 4.2 on 2023-05-03 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('product', '0011_rename_vendors_order_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_by',
        ),
        migrations.AddField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='vendor.vendor'),
        ),
    ]