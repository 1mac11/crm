from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    photo = models.ImageField(null=True)
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=10, null=True)

    def __set_ver_code(self):
        if self.id > 1000:
            return self.id
        return self.id * 101


    def save(self, *args, **kwargs):
        self.verification_code = self.__set_ver_code()
        super().save(*args, **kwargs)

    def __str__(self):
        fname = self.get_full_name()
        if fname:
            return fname
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
