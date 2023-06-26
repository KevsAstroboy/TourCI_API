from django.urls import re_path
from .views import *



urlpatterns = [
    re_path(r'villes/', GetVilleView.as_view()),
    re_path(r'site-touristiques/', GetSiteTouristiqueView.as_view()),
    re_path(r'stades/', GetStadeView.as_view()),
]