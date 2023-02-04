import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from config import settings
from .utils import send_email

USER_TYPE = (
    ("admin", "admin"),
    ("employee", "employee"),
)


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=10, choices=USER_TYPE, default='admin')

    def set_code(self):
        random_number = random.randint(1000, 9999)
        self.verification_code = random_number
        self.save()
        # print(self)
        # print(self.verification_code)
        send_email(
            'Your verification code',
            f'{self.verification_code}',
            settings.FROM_EMAIL,
            [f'{self.email}'],
        )

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
