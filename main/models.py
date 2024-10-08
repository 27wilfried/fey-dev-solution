from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
    
class Realisation(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='realisations/')

    def __str__(self):
        return self.title
    
class Avis(models.Model):
    auteur = models.CharField(max_length=100)
    contenu = models.TextField()
    image_google = models.ImageField(upload_to='images/', blank=True, null=True)  # Image pour Google
    image_avis = models.ImageField(upload_to='images/', blank=True, null=True)    # Image pour les avis

    def __str__(self):
        return self.auteur