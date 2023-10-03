from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50,)
    desc=models.TextField()
    author=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=50)
    message=models.TextField()
    
   
    