from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)

class CustomUserAdmin(UserAdmin):

    list_display = ['username', 'email', 'phone_number', 'date_of_birth', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'phone_number']
    
    # How to order the records
    ordering = ['username']
    
    # Fields to show in the edit form (grouped by section)
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('phone_number', 'profile_picture', 'date_of_birth')
        }),
    )
    
    # Fields to show in the add form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('phone_number', 'profile_picture', 'date_of_birth')
        }),
    )

