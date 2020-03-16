from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Information)
admin.site.register(models.Club)
admin.site.register(models.Match)

