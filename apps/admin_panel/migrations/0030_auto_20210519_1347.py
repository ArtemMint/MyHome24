# Generated by Django 3.1.7 on 2021-05-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0029_auto_20210517_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionpurpose',
            name='type',
            field=models.CharField(choices=[('Приход', 'Приход'), ('Расход', 'Расход')], max_length=150, verbose_name='Приход/Расход'),
        ),
    ]
