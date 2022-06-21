from rest_framework import serializers
from django.conf import settings
from .models import Master, Info, Gallery, Application, Price, Review, Work


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ["name", "image", "description", "image_work"]


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ["name", "info", "telegram", "vk", "phone_number"]


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['image', 'image_status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['client_name', 'client_image', 'client_review', 'tattoo_image']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['client_name', 'contacts', 'tattoo_description', 'sketch']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['tattoo_image', 'price']