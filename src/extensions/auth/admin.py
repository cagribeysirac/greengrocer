from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

admin.site.site_header = "GreenGrocer Admin"
admin.site.site_title = "GreenGrocer Admin Portal"
admin.site.index_title = "Welcome to the GreenGrocer Admin Portal"


class CustomUserAdmin(UserAdmin):
    """Custom admin for the CustomUser model."""

    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone_number',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('phone_number',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
