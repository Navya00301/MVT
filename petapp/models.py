from django.db import models

class Pet(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    image=models.ImageField(upload_to='pets/')

    def __str__ (self):
        return self.name

