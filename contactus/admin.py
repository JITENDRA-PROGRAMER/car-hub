from django.contrib import admin
from jmespath import search

from contactus.models import Contactus
from .models import Contactus
# from jmespath import search 

# Register your models here.
class ContactusAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','car_title','city','state','create_date')
    list_display_links = ('id','first_name','last_name')
    search_fields = ('first_name','last_name','email','car_title','city','state')
    list_per_page = 25
admin.site.register(Contactus,ContactusAdmin) 