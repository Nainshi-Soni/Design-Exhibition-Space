from django.db import models

# Create your models here.
class Portfolios(models.Model):
    port_id=models.IntegerField(primary_key=True)
    port_img=models.ImageField(null=True,upload_to="images/")
    port_link=models.CharField(max_length=50,null=True)
    port_zip=models.FileField(null=True)