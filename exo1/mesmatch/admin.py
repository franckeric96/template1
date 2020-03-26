from django.contrib import admin
from . import models 
from django.utils.safestring import mark_safe

from actions import Actions

# Register your models here.
class MatchAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['image','nom_equip']}),
        ('Standard', {'fields': ['score']}),
        ('Tag', {'fields': ['tag']})
    ]
    
    
    list_display = ('image_views','nom_equip','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom_equip',)
    date_hierarchy = "date_add"
    list_display_links = ['nom_equip']
    ordering = ['nom_equip']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

                                                                                                                                  
    
class InformationAdmin(Actions):
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','nb_match']}),
        ('Standard',{'fields': ['location','icon']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    
class ClubAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['image','nom']}),
        ('Standard', {'fields': ['information_Club','description','nom_player']}),
        ('Tag', {'fields': ['tag']})
    ]
    
    
    list_display = ('image_views','nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Match, MatchAdmin)  
_register(models.Information, InformationAdmin) 
_register(models.Club, ClubAdmin)  
