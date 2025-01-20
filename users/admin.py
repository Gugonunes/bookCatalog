from django.contrib import admin
from users.models import Role, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('bio', 'profile_picture', 'role', 'linkedin_url', 'github_url')
        }),
    )
    list_display = ['username']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
