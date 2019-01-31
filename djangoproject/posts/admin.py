from django.contrib import admin
from posts.models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Stock)
admin.site.register(News)
