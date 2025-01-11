from django.db import models

# Create your models here.
class table(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  image = models.ImageField(upload_to='media')
  email = models.CharField(max_length=50 , default='') 

  def __str__(self):
    return self.firstname 


class posts(models.Model):
  title = models.CharField(max_length=255)
  des = models.CharField(max_length=255)
  image = models.ImageField(upload_to='media') 

  def __str__(self):
    return self.title