# Generated by Django 3.1.6 on 2021-03-31 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210331_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/'),
        ),
    ]
