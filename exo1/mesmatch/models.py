from django.db import models

# Create your models here.

class Information(models.Model):
    ICONS = [
        ("Youtube", "fa-youtube"),
        ("Facebook", "fa-facebook"),
        ("twitter", "fa-twitter"),
        ("Google-plus", "fa-google-plus"),
        ("Instagram", "fa-instagram"),

        
    ]
    
    icon = models.CharField(choices=ICONS, max_length=20)
    nom = models.CharField(max_length=255)
    nb_match = models.IntegerField()
    location = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Information'
        verbose_name_plural = 'Informations'

    def __str__(self):
        return self.nom


class Match(models.Model):
    nom_equip = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Match')
    score = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Match'
        verbose_name_plural = 'Matchs'

    def __str__(self):
        return self.nom_equip
    
    
class Club(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Club')
    information_Club = models.ForeignKey(Information,on_delete=models.CASCADE,related_name='Club_info')
    description = models.TextField()
    nom_player = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.nom