from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin

from .models import CategoryModel, SubcategoryModel, ProductModel, ProductPhotoModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'description')
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget}
    }


admin.site.register(CategoryModel)
admin.site.register(SubcategoryModel)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ProductPhotoModel)
