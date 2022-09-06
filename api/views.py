from django.shortcuts import render
from rest_framework import viewsets, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .models import Master, Info, Gallery, Work, Review, Application, Price, FAQ
from .serializers import MasterSerializer, InfoSerializer, GallerySerializer, \
    WorkSerializer, ReviewSerializer,\
    ApplicationSerializer, PriceSerializer, FAQSerializer


# def send_notification_to_master(instance):
#     application = Application.objects.get(id=instance.id)
#     try:
#         subject = "Новая заявка"
#         to = ['{}'.format(  )]   # email here
#         from_email = # email here
#         email_content = application
#         message = get_template('email/email.html').render(application) #TODO add template
#         msg = EmailMessage(subject, message, to=to, from_email=from_email)
#         msg.content_subtype = 'html'
#         msg.send()
#     except IOError as e:
#         return e

class MasterViewSet(viewsets.ModelViewSet):
    """ main page """
    serializer_class = MasterSerializer
    queryset = Master.objects.all()

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        # using 'first' will retrieve first instance
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class InfoViewSet(viewsets.ModelViewSet):
    """ info """
    serializer_class = InfoSerializer
    queryset = Info.objects.all()

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        # using 'first' will retrieve first instance
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FAQViewSet(viewsets.ModelViewSet):
    """ FAQ """
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class GalleryViewSet(viewsets.ModelViewSet):
    """ gallery """
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class WorkViewSet(viewsets.ModelViewSet):
    """ work examples """
    serializer_class = WorkSerializer
    queryset = Work.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    """ clients' reviews"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ApplicationViewSet(viewsets.ModelViewSet):
    """ tattoo application """
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     try:
    #         send_email_confirmation(modified=instance)
    #         print('An email has been sent to the customer.')
    #     except IOError as e:
    #         return e


class PriceViewSet(viewsets.ModelViewSet):
    """ prices page """
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
