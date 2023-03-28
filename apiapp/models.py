from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12,unique=True, null=False)
    date_of_birth = models.DateTimeField(null= True)
    reset_code = models.CharField(max_length=10, null=True)

    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return f"{self.phone_number} - {self.username}"



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
