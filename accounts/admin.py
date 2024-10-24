from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role']  # Add any other fields you want to display
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  # Include the role field in the admin form
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),  # Include the role field in the add user form
    )

admin.site.register(CustomUser, CustomUserAdmin)
