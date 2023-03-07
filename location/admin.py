from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Location, LocationImages


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'company', 'company_owner')
    ordering = ['id']
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address')
    list_filter = ('company',)
    filter_horizontal = ('employee',)
    autocomplete_fields = ('company',)
    list_per_page = 50  # No of records per page

    def company_owner(self, obj):
        return f'{obj.company.owner} id={obj.company.owner.id}'

    company_owner.short_description = _('Company owner')



class LocationImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'location_company', 'location_company_owner', 'get_html_photo')
    ordering = ['id']
    list_display_links = ('id', 'title')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    readonly_fields = ('get_html_photo',)
    autocomplete_fields = ('location',)

    def get_html_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src = "{obj.image.url}" width = "300"/>')

    get_html_photo.short_description = _('image')
    get_html_photo.allow_tags = True

    def location_company(self, obj):
        return f'{obj.location.company} id={obj.location.company.id}'

    location_company.short_description = _('company of location')

    def location_company_owner(self, obj):
        return f'{obj.location.company.owner} id={obj.location.company.owner.id}'

    location_company_owner.short_description = _('location company owner')


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationImages, LocationImagesAdmin)
