from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail

from .models import Application

def send_email(app_info):
    subject = 'New application'
    message = f'You have a new application from {app_info.client_name} at {app_info.datetime}. Text: {app_info.tattoo_description}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['riveriswild.rw@gmail.com', ]
    print('sent')
    send_mail(subject, message, email_from, recipient_list)

@receiver(post_save, sender=Application)
def create_new_application(sender, instance, created, **kwargs):
    if created:
        print(created)
        app_info = instance
        send_email(app_info)