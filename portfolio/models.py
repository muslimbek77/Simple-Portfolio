from distutils.command.upload import upload
from django.db import models

# Create your models here.



class Home(models.Model):
    title = models.CharField(max_length=100)
    thumb_image = models.ImageField()
    image = models.ImageField()
    my_job = models.TextField(max_length=200)
    content = models.TextField(max_length=200)


class About(models.Model):
    my_story = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_quare = models.ImageField()
    full_image = models.ImageField()
    
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    year_of_experiences = models.CharField(max_length=50)
    happy_costumers = models.CharField(max_length=50)
    digital_awards = models.CharField(max_length=50)
    project_finished = models.CharField(max_length=50)







class Project(models.Model):
    job = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

class Services(models.Model):
    service_tag = models.CharField(max_length=50)
    def __str__(self):
        return self.service_tag
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    service = models.ManyToManyField(Services)
    text = models.TextField()
    
