# Generated by Django 4.1.7 on 2023-03-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_categorymodel_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='main_photo',
            field=models.ImageField(null=True, upload_to='product/'),
        ),
    ]
