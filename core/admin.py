from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role, School, ManualMpesaDonation


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'full_name', 'role', 'school', 'is_verified', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'role', 'is_verified', 'school')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    # Remove 'school' from readonly_fields so it is always editable
    readonly_fields = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'role', 'school')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'role', 'school', 'is_verified', 'is_staff', 'is_active')}
        ),
    )
    # Remove get_readonly_fields so school is always editable


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'location', 'email', 'phone_number', 'created_at')
    search_fields = ('school_name', 'location', 'email', 'phone_number')
    ordering = ('school_name',)


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(School, SchoolAdmin)
admin.site.register(ManualMpesaDonation)
