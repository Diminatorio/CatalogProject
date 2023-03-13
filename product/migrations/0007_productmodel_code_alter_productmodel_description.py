# Generated by Django 4.1.7 on 2023-03-09 10:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_productphotomodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='code',
            field=models.CharField(default='SHK', max_length=50),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]