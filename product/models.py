from django.db import models

from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    photo = models.ImageField(upload_to='category/', null=True)
    category_name = models.CharField(unique=True, max_length=15)


class SubcategoryModel(models.Model):
    category_id = models.ForeignKey('CategoryModel', verbose_name="CATEGORY_ID", on_delete=models.DO_NOTHING)
    subcategory_name = models.CharField(unique=True, max_length=20)
    photo = models.ImageField(upload_to='subcategory/', null=True)


class ProductModel(models.Model):
    subcategory_id = models.ForeignKey('SubcategoryModel', verbose_name="CATEGORY_ID", on_delete=models.DO_NOTHING)
    main_photo = models.ImageField(upload_to='product/', null=True)
    product_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = RichTextField(null=True, blank=True)
    code = models.CharField(max_length=50, default='SHK')


class ProductPhotoModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='product/')
