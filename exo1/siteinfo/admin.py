from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions import Actions

# Register your models here.
class AcceuilAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Standard', {'fields': ['description','lien']}),
        ('reseaux', {'fields': ['icon','new','status']})
        
    ]
    
    
    list_display = ('image_views','titre','date_add','status')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

                                                                                                                                  
    
class LocalisationAdmin(Actions):
    
    fieldsets = [
        ('Presentation',{'fields': ['address','description']}),
        ('Status',{'fields': ['site_map','status']})
       
    ]
    
    list_display = ('address','date_add','status')
    list_filter = ('status',)
    search_fields = ('address',)
    date_hierarchy = "date_add"
    list_display_links = ['address']
    ordering = ['address']
    list_per_page = 10
    


    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Acceuil, AcceuilAdmin)  
_register(models.Localisation, LocalisationAdmin) 
 