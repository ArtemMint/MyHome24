# Generated by Django 3.1.7 on 2021-05-21 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0030_auto_20210519_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.tariff', verbose_name='Тариф'),
        ),
    ]