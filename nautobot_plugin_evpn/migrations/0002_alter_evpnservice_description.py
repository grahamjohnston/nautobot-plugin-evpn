# Generated by Django 3.2.15 on 2022-09-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_plugin_evpn", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evpnservice",
            name="description",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
    ]
