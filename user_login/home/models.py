from django.db import models

# Create your models here.
class User_data(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.name