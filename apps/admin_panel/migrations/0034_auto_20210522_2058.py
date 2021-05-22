# Generated by Django 3.1.7 on 2021-05-22 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0033_accounttransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttransaction',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_transactions_managers', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер'),
        ),
        migrations.AlterField(
            model_name='accounttransaction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_transactions_owners', to=settings.AUTH_USER_MODEL, verbose_name='Владелец квартиры'),
        ),
    ]