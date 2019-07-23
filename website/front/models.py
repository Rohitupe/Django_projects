from django.db import models

# Create your models here.
class Contact(models.Model):
    db_name = models.CharField(max_length = 50)
    db_email = models.EmailField()
    db_message = models.TextField()

    def __str__(self):
        return self.db_name
