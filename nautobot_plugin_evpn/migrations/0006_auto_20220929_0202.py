# Generated by Django 3.2.15 on 2022-09-29 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_plugin_evpn', '0005_auto_20220923_0328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evpnservice',
            options={'verbose_name': 'EVPN Service', 'verbose_name_plural': 'EVPN Services'},
        ),
        migrations.RemoveField(
            model_name='evpnservice',
            name='vni',
        ),
    ]