from django.contrib import admin

from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'role', 'avatar', 'date_joined']


admin.site.register(User, UserAdmin)