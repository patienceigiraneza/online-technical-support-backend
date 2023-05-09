from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Supporter)
admin.site.register(Board)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Category)
admin.site.register(SubCategory)
