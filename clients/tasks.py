from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from clients.models import Clients


@shared_task()
def send_email_task(company_id, title, message, from_email):
    email_adresses = list(Clients.objects.filter(bought_products__company_id=company_id).values_list('email', flat=True))
    # print(email_adresses)
    sleep(10)

    send_mail(
        title,
        message,
        'rajrajrajradju@gmail.com',
        email_adresses,
        fail_silently=False,
    )
    # print('emails sent succesfully')
    return "Done"
