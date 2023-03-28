from django.db import models



class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()

class Client(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=244)
    address = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=244)

class Supporter(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=244)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Conversation(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
    supporter_id = models.ForeignKey(Supporter, on_delete= models.CASCADE)
    title = models.CharField(max_length=255)

class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.PROTECT)
    sender = 