from django.contrib import admin
from .models import LocalInventory, GlobalInventory

class LocalInventoryInline(admin.StackedInline):
    model = LocalInventory
    extra = 2

class GlobalInventoryAdmin(admin.ModelAdmin):
    model = GlobalInventory
    inlines = [LocalInventoryInline]

admin.site.register(GlobalInventory, GlobalInventoryAdmin)
