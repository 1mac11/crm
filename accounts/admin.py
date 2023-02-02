from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'email_verified', 'type')
    ordering = ['id']
    list_display_links = ('id', 'username')
    search_fields = ('username', 'first_name', 'last_name')
    list_editable = ('email_verified',)
    list_filter = ('email_verified', 'type')


admin.site.register(User, UserAdmin)
