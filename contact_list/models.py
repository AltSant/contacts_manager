from django.db import models

# Create your models here.

class Contact(models.Model):

    full_name = models.CharField(max_length=60)
    birth_date = models.DateField(max_length=8)

    def publish(self):
        self.save()

    def __str__(self):
        return self.full_name    