# Generated by Django 2.2.5 on 2019-10-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(verbose_name='Год издания'),
        ),
    ]
