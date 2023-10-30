from django.contrib import admin

from .models import Product, ProductImage, Collection

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'price', 'collection']}),
    ]
    inlines = [ProductImageInline]
    list_display = ('name', 'price', 'collection')
    list_filter = ['price']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
