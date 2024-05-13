from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    link = models.TextField()
    image = models.ImageField(upload_to='files/projects')

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(blank=False, null=False)
    

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    logo = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=100)
    subject = models.TextField(max_length=500)
    date = models.CharField(max_length=90)

    def __str__(self):
        return self.title