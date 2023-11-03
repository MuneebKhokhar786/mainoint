from django.contrib import admin

from .models import Product, ProductImage, ProductVideo, Collection

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'price', 'collection']}),
    ]
    inlines = [ProductImageInline, ProductVideoInline]
    list_display = ('name', 'price', 'collection')
    list_filter = ['price']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
