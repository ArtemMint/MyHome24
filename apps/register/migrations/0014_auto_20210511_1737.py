# Generated by Django 3.1.7 on 2021-05-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20210511_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=1500, verbose_name='notes about'),
        ),
    ]