# Generated by Django 2.2.5 on 2019-11-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20191112_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='1', null=True, upload_to='books/images'),
        ),
    ]
