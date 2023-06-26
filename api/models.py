from django.db import models

# Create your models here.
class Ville(models.Model):
    nom_ville = models.CharField(max_length=50, null=False)
    description_ville = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    video_ville = models.CharField(max_length=1000, null=True)
    historique_ville = models.CharField(max_length=2000, null=True)
    atouts_ville = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.nom_ville


class SiteTouristique(models.Model):
    nom_site = models.CharField(max_length=50, null=False)
    description_site = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    video_site = models.CharField(max_length=2000, null=True)
    historique_site = models.CharField(max_length=2000, null=True)
    atouts_site = models.CharField(max_length=1000, null=True)
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nom_site
    

class Stade(models.Model):
    nom_stade = models.CharField(max_length=50, null=False)
    description_stade = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    video_stade = models.CharField(max_length=2000, null=True)
    ville = models.OneToOneField(Ville,on_delete=models.CASCADE,null=False)

    def __str__(self) -> str:
        return self.nom_stade


class VillePhoto(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='photos')

class StadePhoto(models.Model):
    stade = models.ForeignKey(Stade, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='photos')
    

class SiteTouristiquePhoto(models.Model):
    site_touristique = models.ForeignKey(SiteTouristique, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='photos')
