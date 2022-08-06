from django.urls import path
from .views import MasterViewSet, GalleryViewSet, InfoViewSet, WorkViewSet, \
    ReviewViewSet, ApplicationViewSet, PriceViewSet, FAQViewSet

"""
CLIENT
base endpoint /api/
"""
urlpatterns = [
    path('', MasterViewSet.as_view({'get': 'list'})),
    path('gallery/', GalleryViewSet.as_view({'get': 'list'})),
    path('info/', InfoViewSet.as_view({'get': 'list'})),
    path('works/', WorkViewSet.as_view({'get': 'list'})),
    path('reviews/', ReviewViewSet.as_view({'get': 'list'})),
    path('application/', ApplicationViewSet.as_view({'get': 'list'})),
    path('prices/', PriceViewSet.as_view({'get': 'list'})),
    path('faq/', FAQViewSet.as_view({'get': 'list'}))
]
