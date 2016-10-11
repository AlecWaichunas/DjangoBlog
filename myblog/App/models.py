from django.db import models

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_text = models.CharField(max_length=none)
    blog_date = models.DateField()
    
