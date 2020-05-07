from django.db import models
from django.utils import timezone

# Create your models here.
class Trending(models.Model):
    category= models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    address=models.TextField()
    title=models.CharField(max_length=200)

class FindBusiness(models.Model):
    category= models.ForeignKey('category',on_delete=models.CASCADE)
    img=models.ImageField(upload_to='pics1')
    clas = models.CharField(max_length=30)
    


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
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=200)
    landmark=models.CharField(max_length=100)
    website=models.URLField(max_length=200)
    Description=models.TextField()
    image=models.ImageField(upload_to='pics')
    created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.business_name

class category(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name


class mailing(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=80)
    message=models.TextField()

    def __str__(self):
        return self.email


class Donor_Register(models.Model):
    donorname=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    bloodcategory = models.ForeignKey('bloodcategory',on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    pincode=models.IntegerField()
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.donorname

class bloodcategory(models.Model):
    name = models.CharField(max_length=6)
    
    
    def __str__(self):
        return self.name


class DonorMessage(models.Model):
    email1=models.EmailField(max_length=100)
    email2=models.EmailField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.email2