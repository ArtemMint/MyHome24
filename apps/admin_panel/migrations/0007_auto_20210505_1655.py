# Generated by Django 3.1.7 on 2021-05-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_auto_20210505_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='editing_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]