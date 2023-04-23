from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Supporter)
admin.site.register(Board)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Category)
admin.site.register(SubCategory)
