from django.db import models

# Create your models here.
class Contact(models.Model):
    db_name = models.CharField(max_length = 50)
    db_email = models.EmailField()
    db_message = models.TextField()

    def __str__(self):
        return self.db_name

class Image(models.Model):
    image_name = models.CharField(max_length =50)
    image_file = models.ImageField(upload_to = 'gallery_images')

    def __str__(self):
        return self.image_name
