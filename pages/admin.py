from re import search
from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

# Make coustem database designing 
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"  />'.format(object.photo.url))
     
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail','firstname', 'lastname', 'designation', 'created_date')
    list_display_links = ('id','thumbnail','firstname')
    search_fields = ('firstname','lastname','designation')
    list_filter = ('designation',)


admin.site.register(Team,TeamAdmin) #Register model