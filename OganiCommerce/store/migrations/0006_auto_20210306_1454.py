# Generated by Django 3.1.6 on 2021-03-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210306_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/'),
        ),
    ]
