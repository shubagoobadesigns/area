from django.core.mail import send_mail
from django.conf import settings


def send_from_default_email(subject, message, recipient_list, **kwargs):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, **kwargs)
