from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import AdminUserCreationForm, AdminUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = AdminUserCreationForm
    form = AdminUserChangeForm
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets =  UserAdmin.fieldsets + (
        (None, {
            "classes": ("wide",),
            "fields": (
                "address", "city", "country", "zip_code", "phone_number",
            )}
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "address", "city", "country", "zip_code", "phone_number")}),
        ("Dates", {"fields": ("last_login", "date_joined"), }),

    )

admin.site.register(CustomUser, CustomUserAdmin)
