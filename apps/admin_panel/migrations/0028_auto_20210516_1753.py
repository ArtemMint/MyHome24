# Generated by Django 3.1.7 on 2021-05-16 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0027_auto_20210516_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ('-editing_date',)},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'ordering': ('-editing_date',)},
        ),
        migrations.AddField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='editing_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='editing_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]