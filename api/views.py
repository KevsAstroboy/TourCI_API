from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *


# Create your views here.

class GetVilleView(APIView):
    def get(self, request, *args, **kwargs):
        villes = Ville.objects.all()
        response = []

        for ville in villes:
            photos = []
            ville_photos = VillePhoto.objects.filter(ville=ville.id)
            for photo in ville_photos:
                photoo = {
                    "id": str(photo.id),
                    "photo_ville": str(photo.photo)
                }
                photos.append(photoo)

            responseJson = {
                "id": str(ville.id),
                "nom_ville": str(ville.nom_ville),
                "description_ville": str(ville.description_ville),
                "video_ville": str(ville.video_ville),
                "historique_ville": str(ville.historique_ville),
                "atouts_ville": str(ville.atouts_ville),
                "photos_ville": photos
            } 
            response.append(responseJson)

        return Response({"hasError": False, "data": response}, status=status.HTTP_200_OK)


class GetSiteTouristiqueView(APIView):
    def get(self, request, *args, **kwargs):
        sites = SiteTouristique.objects.all()
        response = []

        for site in sites:
            photos = []
            site_photos = SiteTouristiquePhoto.objects.filter(site_touristique=site.id)
            for photo in site_photos:
                photoo = {
                    "id": str(photo.id),
                    "photo_site": str(photo.photo)
                }
                photos.append(photoo)

            responseJson = {
                "id": str(site.id),
                "nom_site": str(site.nom_site),
                "description_site": str(site.description_site),
                "video_site": str(site.video_site),
                "historique_site": str(site.historique_site),
                "atouts_site": str(site.atouts_site),
                "photos_site": photos
            } 
            response.append(responseJson)

        return Response({"hasError": False, "data": response}, status=status.HTTP_200_OK)



class GetStadeView(APIView):
    def get(self, request, *args, **kwargs):
        stades = Stade.objects.all()
        response = []

        for stade in stades:
            photos = []
            stade_photos = StadePhoto.objects.filter(stade=stade.id)
            for photo in stade_photos:
                photoo = {
                    "id": str(photo.id),
                    "photo_ville": str(photo.photo)
                }
                photos.append(photoo)

            responseJson = {
                "id": str(stade.id),
                "nom_stade": str(stade.nom_stade),
                "description_stade": str(stade.description_stade),
                "video_stade": str(stade.video_stade),
                "photos_stade": photos
            } 
            response.append(responseJson)

        return Response({"hasError": False, "data": response}, status=status.HTTP_200_OK)