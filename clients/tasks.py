from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_email_task(message):
    sleep(20)  # Simulate expensive operation(s) that freeze Django

    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        'email_addresses list',
        fail_silently=False,
    )
