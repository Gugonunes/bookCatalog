from django.contrib import admin
from users.models import Role, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
