# Generated by Django 5.0.1 on 2024-12-22 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Rent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.applications'),
        ),
    ]
