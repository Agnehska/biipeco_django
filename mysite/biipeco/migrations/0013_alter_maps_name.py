# Generated by Django 4.0.6 on 2022-07-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biipeco', '0012_maps_menu_alter_talks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Регион'),
        ),
    ]
