# Generated by Django 4.1.7 on 2023-03-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productmodel_remove_categorymodel_photo_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='photo',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='productphotomodel',
            name='image',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='subcategorymodel',
            name='photo',
            field=models.ImageField(null=True, upload_to='subcategory/'),
        ),
    ]
