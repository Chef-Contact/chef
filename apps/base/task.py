from celery import shared_task
from django.core.mail import send_mail
from .models import Contact

@shared_task
def send_contact_email(last_name, email, number, message):
    Contact.objects.create(last_name=last_name, email=email, number=number, message=message)
    
