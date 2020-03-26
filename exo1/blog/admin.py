from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe



# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Standard', {'fields': ['auteur','contenu','categorie_article']}),
        ('Tag', {'fields': ['tag']}),
        ('Status', {'fields': ['status']})
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

class  ArticleInline(admin.TabularInline):
    model = models.Categorie  
    extra = 0                                                                                                                                 

class CategorieAdmin(admin.ModelAdmin):
   
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','description']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    Inlines = [ArticleInline]
    
    
    actions = ('active','deactive')
    def active(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'domi a modifier La selection a été deactivé avec succès')

    active.short_description = 'Desactiver'

    def deactive(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'La selection a été activé avec succès')

    deactive.short_description = 'Activer'
    

    
class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['nom','description']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    
    list_display = ('nom','description','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
class CommentaireAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['nom']}),
        ('Contenu',{'fields': ['article','site','commentaire']}),
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

_register(models.Article, ArticleAdmin)  
_register(models.Categorie, CategorieAdmin) 
_register(models.Commentaire, CommentaireAdmin)  
_register(models.Tag, TagAdmin)   




