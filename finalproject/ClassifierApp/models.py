from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/')
    
    def __str__(self):
        return self.title + ' ' + self.image.path
