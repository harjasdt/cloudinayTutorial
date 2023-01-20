from django.db import models
from cloudinary.models import CloudinaryField

class Photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image=models.ImageField()
    cc = CloudinaryField('image')