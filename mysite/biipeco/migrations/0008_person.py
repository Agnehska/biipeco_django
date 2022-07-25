# Generated by Django 4.0.6 on 2022-07-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biipeco', '0007_needs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
                ('email', models.CharField(max_length=200, verbose_name='Почта')),
                ('whatsapp', models.CharField(max_length=200, verbose_name='Whatsapp')),
                ('telegram', models.CharField(max_length=200, verbose_name='Telegram')),
                ('img', models.FileField(upload_to='img/main/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
