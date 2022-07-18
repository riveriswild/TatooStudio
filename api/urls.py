from django.contrib import admin
from django.urls import path
from .views import MasterViewSet, GalleryViewSet, InfoViewSet, WorkViewSet, ReviewViewSet, ApplicationViewSet, PriceViewSet

"""
CLIENT
base endpoint /api/
"""
urlpatterns = [
    path('', MasterViewSet.as_view()),
    path('gallery/', GalleryViewSet.as_view()),
    path('info/', InfoViewSet.as_view()),
    path('works/', WorkViewSet.as_view()),
    path('reviews/', ReviewViewSet.as_view()),
    path('application/', ApplicationViewSet.as_view()),
    path('prices/', PriceViewSet.as_view())
]