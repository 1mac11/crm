from django.core.mail import send_mail
from .models import Clients


def send_emails(company_id, title, text, from_email):

    clients = Clients.objects.filter(bought_products__company_id=company_id)

    for client in clients:
        send_mail(title, text, from_email, client.email, fail_silently=False, )
