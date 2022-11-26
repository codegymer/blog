from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here

class User(AbstractUser):
    udp = models.ImageField(default='udp_pics/udpdefault.jpg', upload_to='udp_pics',null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    # phone_number = models.CharField(max_length=12,blank=True)
    # pincode = models.CharField(max_length=6, blank=True)
    # address = models.CharField(max_length=500, blank=True)
    # state = models.CharField(max_length=20, blank=True)



class Post(models.Model):
    user=models.ForeignKey(

        User,on_delete=models.CASCADE,

    )
    title=models.CharField(max_length=100)
    highlight=models.CharField(default='Highlight Not Provided!',max_length=1000,null=True)
    postpic= models.ImageField(default='post_pics/postdefault.jpg', upload_to='post_pics',null=True, blank=True)

    content=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)