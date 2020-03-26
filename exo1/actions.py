
from django.contrib import admin


class Actions(admin.ModelAdmin):
    
    actions = ('active','deactive')
    def active(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'La selection a été deactivé avec succès')

    active.short_description = 'Desactiver'

    def deactive(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'La selection a été activé avec succès')

    deactive.short_description = 'Activer'
    