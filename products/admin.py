from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Product Admin"""
    list_display = (
        'sku',
        'name',
        'element',
        'category',
        'price',
        'rating',
        'image_1',
        'image_2',
        'image_3',
        'image_4',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """category admin"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
