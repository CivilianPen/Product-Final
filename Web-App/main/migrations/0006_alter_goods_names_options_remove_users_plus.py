# Generated by Django 5.0.1 on 2025-01-24 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_goods_goods'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods_names',
            options={'verbose_name': 'Название инвентаря', 'verbose_name_plural': 'Названия инвентаря'},
        ),
        migrations.RemoveField(
            model_name='users',
            name='Plus',
        ),
    ]
