# Generated by Django 3.1.7 on 2021-04-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210428_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='notes about'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('Директор', 'Директор'), ('Управляющий', 'Управляющий'), ('Бухгалтер', 'Бухгалтер'), ('Электрик', 'Электрик'), ('Сантехник', 'Сантехник')], max_length=150, null=True, verbose_name='role of the user'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('Активен', 'Активен'), ('Новый', 'Новый'), ('Отключен', 'Отключен')], max_length=100, null=True, verbose_name='status of user'),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='telegram'),
        ),
        migrations.AddField(
            model_name='user',
            name='viber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='viber'),
        ),
    ]
