from django.contrib import admin

from .models import Notifications


class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'read_status', 'created_time')
    ordering = ['id']
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    autocomplete_fields = ('company',)
    list_per_page = 50  # No of records per page


admin.site.register(Notifications, NotificationsAdmin)
