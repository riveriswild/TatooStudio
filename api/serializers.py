from rest_framework import serializers
from django.conf import settings
from .models import Master, Info, Gallery, Application, Price, Review, Work


class MasterSerializer(serializers.ModelSerializer):
    """
    serializer for master's page info
    """
    class Meta:
        model = Master
        fields = ["name", "image", "description", "image_work"]


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ["name", "info", "telegram", "vk", "phone_number"]


class GallerySerializer(serializers.ModelSerializer):
    """
    Serializer for photos in gallery on main page
    """
    class Meta:
        model = Gallery
        fields = ['image']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['image', 'image_status']


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for reviews
    """
    class Meta:
        model = Review
        fields = ['client_name', 'client_image', 'client_review', 'tattoo_image']


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer to use in an application form
    """
    class Meta:
        model = Application
        fields = ['client_name', 'contacts', 'tattoo_description', 'sketch']


class PriceSerializer(serializers.ModelSerializer):
    """
    Serializer for prices
    """
    class Meta:
        model = Price
        fields = ['tattoo_image', 'price']