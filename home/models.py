from django.db import models

# Create your models here.
class Trending(models.Model):
    category= models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    address=models.TextField()
    title=models.CharField(max_length=200)

class FindBusiness(models.Model):
    title= models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics1')


class UserRegister(models.Model):
    firstname=models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=100)


    def __str__(self):
        return self.username

class Business_detail(models.Model):
    firstname=models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=100)


    def __str__(self):
        return self.username

class Business_List(models.Model):
    business_name=models.CharField(max_length=50)
    pincode = models.IntegerField()
    email=models.EmailField(max_length=200)
    category=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=200)
    landmark=models.CharField(max_length=100)
    website=models.URLField(max_length=200)
    Description=models.TextField()
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.business_name