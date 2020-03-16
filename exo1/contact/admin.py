from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe



# Register your models here.                                                                                                                                
    
class ContactAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','email']}),
        ('Message',{'fields': ['message']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    


    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)
  
_register(models.Contact, ContactAdmin)  
