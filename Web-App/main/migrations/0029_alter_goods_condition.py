# Generated by Django 5.0.1 on 2025-01-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_applications_repair_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='condition',
            field=models.CharField(choices=[('новый', 'новый'), ('использованный', 'использованный'), ('сломанный', 'сломанный')], max_length=20, verbose_name='Состояние'),
        ),
    ]
