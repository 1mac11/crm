from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'email', 'phone')
    ordering = ['id']
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    filter_horizontal = ('employee',)
    autocomplete_fields = ('owner',)
    list_per_page = 50  # No of records per page


admin.site.register(Company, CompanyAdmin)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)
