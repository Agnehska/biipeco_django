# Generated by Django 4.0.6 on 2022-07-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biipeco', '0009_specializations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specializations',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Специализация'),
        ),
    ]