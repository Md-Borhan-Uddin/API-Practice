from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    created = models.DateTimeField(auto_now=True)  
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    