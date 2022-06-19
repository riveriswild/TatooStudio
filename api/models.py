from django.db import models


class Master(models.Model):
    """
    Tattoo artists main info
    """
    image = models.FileField(upload_to='images/', blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image_work = models.FileField(upload_to='images/', blank=True, null=True)


class Gallery(models.Model):
    """
    Image for a gallery
    """
    image = models.FileField(upload_to='images/', blank=True, null=True)


class Works(models.Model):
    """
    All works
    """

    NEW = 'new'
    OLD = 'old'
    SKETCH = 'sketch'

    IMAGE_CHOICES = [
        (NEW, 'new'),
        (OLD, 'old'),
        (SKETCH, 'sketch'),
    ]

    image = models.FileField(upload_to='images/', blank=True, null=True)
    image_status = models.CharField(choices=IMAGE_CHOICES, max_length=8, default=NEW, verbose_name='status')


class Review(models.Model):
    """
    Clients' reviews
    """
    client_image = models.FileField(upload_to='images/', blank=True, null=True)
    tatoo_image = models.FileField(upload_to='images/', blank=True, null=True)
    client_name = models.CharField(max_length=124, verbose_name='Имя клиента')
    client_review = models.TextField(max_length=255, blank=True, null=True)   #TODO CHANGE BLANKS AND NULLS


class Application(models.Model):
    """
    Application form for a tattoo
    """
    client_name = models.CharField(max_length=255, null=False, blank=False)
    contacts = models.CharField(max_length=255, null=False, blank=False)
    tattoo_description = models.TextField(max_length=255, null=True, blank=True)
    sketch = models.FileField(upload_to='images/', blank=True, null=True)


# Create your models here.
