from django.shortcuts import render
from rest_framework import viewsets

from .models import Master, Info, Gallery, Work, Review, Application, Price
from .serializers import MasterSerializer,InfoSerializer, GallerySerializer, \
    WorkSerializer, ReviewSerializer,\
    ApplicationSerializer, PriceSerializer


class MasterViewSet(viewsets.ModelViewSet):
    serializer_class = MasterSerializer
    queryset = Master.objects.get(id=1)


class InfoViewSet(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ApplicationViewSet(viewsets.ModelView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class PriceViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()



# Create your views here.
