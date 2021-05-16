# Generated by Django 3.1.7 on 2021-05-16 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0023_auto_20210512_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.housefloor', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.house', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.housesection', verbose_name='Секция'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.tariff', verbose_name='Тариф  '),
        ),
    ]
