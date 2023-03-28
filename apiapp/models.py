from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    PRIORITY_CHOICES = (
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
    )
    STATUS_CHOICES = (
        ('1', 'New'),
        ('2', 'In Progress'),
        ('3', 'Resolved'),
        ('4', 'Closed'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    attachments = models.ManyToManyField('Attachment', blank=True)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.file.name

class Comment(models.Model):
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.body



class TicketAssignment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True)

class TicketNote(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    body = models.TextField()
    def __str__(self):
        return self.body
