import imp
from django.contrib import admin
# from django.contrib.auth.models import User
from .models import Post,User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

# admin.site.register(User)
admin.site.register(Post)
admin.site.register(User,UserAdmin)

