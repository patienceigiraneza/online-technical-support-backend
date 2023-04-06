from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

str_usertype =(
    ("client","client"),
    ("support","support"),
    ("board","board")
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12,unique=True, null=False)
    account_type = models.CharField(max_length=20, choices=str_usertype, default='client')
    reset_code = models.CharField(max_length=10, null=True)

    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return f"{self.phone_number} - {self.username}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=45)

    def __str__(self):
        return self.user

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.category} -- {self.name}"

class Supporter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user} -- {self.category}"

class Board(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    post = models.CharField(max_length=45)


    def __str__(self):
        return f"{self.user} -- {self.post}"

class Conversation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    supporter = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} -- {self.client} -- {self.supporter}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, null=False)
    sender = models.CharField(max_length=20, null=False, choices=str_usertype)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.sender} "

