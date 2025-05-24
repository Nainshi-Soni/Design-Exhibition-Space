from django.db import models

# Create your models here.
class Portfolios(models.Model):
    port_id=models.IntegerField(primary_key=True)
    port_img=models.ImageField(null=True,upload_to="images/")
    port_link=models.CharField(max_length=50,null=True)
    port_zip=models.FileField(null=True,upload_to="file/",blank=True)

class Cards(models.Model):
    card_id=models.IntegerField(primary_key=True)
    card_img=models.ImageField(null=True,upload_to="images/")
    card_link=models.CharField(max_length=50,null=True)
    card_file=models.FileField(null=True,upload_to="file/",blank=True)

class Resumes(models.Model):
    resu_id=models.IntegerField(primary_key=True)
    resu_img=models.ImageField(null=True,upload_to="images/")
    resu_link=models.CharField(max_length=50,null=True)
    resu_file=models.FileField(null=True,upload_to="file/",blank=True)

class Createaccount(models.Model):
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=100)
    contactno=models.CharField(max_length=15)
    passw=models.CharField(max_length=50)
    cpassw=models.CharField(max_length=50)
    date=models.DateField(max_length=30)
