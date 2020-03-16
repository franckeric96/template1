from django.db import models

# Create your models here.
class Acceuil(models.Model):
    ICONS = [
        ("Vimeo", "fa-vimeo"),
        ("Facebook", "fa-facebook"),
        ("twitter", "fa-twitter"),
        ("Google-plus", "fa-google-plus"),
        ("Instagram", "fa-instagram"),

        
    ]
    
    titre = models.CharField(max_length=255)
    icon = models.CharField(choices=ICONS, max_length=20)
    image = models.ImageField(upload_to="images/Acceuil")
    description = models.TextField()
    lien = models.URLField()
    new = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Acceuil'
        verbose_name_plural = 'Acceuils'

    def __str__(self):
        return self.titre
    
    

class Localisation(models.Model):
    address = models.CharField(max_length=255)
    description = models.TextField()
    site_map = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Localisation'
        verbose_name_plural = 'Localisations'

    def __str__(self):
        return self.address