# Generated by Django 3.1.7 on 2021-05-16 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0024_auto_20210516_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(max_length=100, unique=True, verbose_name='№')),
                ('status', models.CharField(choices=[('Активен', 'Активен'), ('Неактивен', 'Неактивен')], max_length=25, verbose_name='Статус')),
                ('account_balance', models.FloatField(default=0, max_length=50, verbose_name='Остаток')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='admin_panel.flat', verbose_name='Квартира')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='admin_panel.house', verbose_name='Дом')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='admin_panel.housesection', verbose_name='Секция')),
            ],
        ),
    ]
