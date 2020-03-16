from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom






class Article(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Article')
    Auteur = models.CharField(max_length=255)
    contenu = models.TextField()
    categorie_article = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie_article')
    tag = models.ManyToManyField(Tag, related_name='tag_Article')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaire_article')
    nom = models.CharField(max_length=255)
    site = models.URLField()
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.nom

    
    