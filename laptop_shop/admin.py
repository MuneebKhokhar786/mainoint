from django.contrib import admin

from .models import Product, ProductImage, ProductVideo, Collection, Order, OrderItem

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

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    exclude = ['product']
    readonly_fields = ['product_name', 'product_description', 'product_price', 'quantity']

    def product_name(self, instance):
        return instance.product.name

    def product_description(self, instance):
        return instance.product.description

    def product_price(self, instance):
        return instance.product.price

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    readonly_fields = ['user', 'total_price', 'payment_method']
    list_filter = readonly_fields
    search_fields = readonly_fields



admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Collection)
