from django.db import models
from django.contrib.auth.models import User
from olx.models import Category

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='userprofile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile',null=True,blank=True)
    address = models.TextField(blank=True)
    mail = models.EmailField(blank=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
    

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    description = models.TextField()
    img = models.ImageField(upload_to='adsimg')
    price = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100,null=True)
    carousel1 = models.ImageField(upload_to='ads/',null=True)
    carousel2 = models.ImageField(upload_to='ads/',null=True)
    carousel3 = models.ImageField(upload_to='ads/',null=True)

    def __str__(self):
        return self.title
    

# class Interested(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     message = models.TextField()

class Interested(models.Model):
    ad = models.ForeignKey(Posts, on_delete=models.CASCADE,null=True) 
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interested_user',null=True)  
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ad_owner',null=True) 
    message = models.TextField(null=True)
    

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} on {self.ad.title}"
