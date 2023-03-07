from django.core.mail import send_mail


def send_email(title, ver_code, from_email, to_email):
    send_mail(title, ver_code, from_email, [to_email], fail_silently=False, )
