from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

# Custme Datatabase like Thumbnale seach field
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"  />'.format(object.car_photo.url))
     
    thumbnail.short_description = 'Car photo'

    list_display = ('id','thumbnail','car_title','city','color','model','year','price','body_style','fule_type','is_feature')
    list_display_links = ('id','thumbnail','car_title')
    search_fields = ('id','car_title','model','year','city','fule_type')
    list_filter = ('car_title','color','fule_type','city')
    list_editable = ('is_feature',)

admin.site.register(Car,CarAdmin) 