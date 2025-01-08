from django.db import models

# Create your models here.
class table(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  image = models.ImageField(upload_to='media')
