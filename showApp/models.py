from django.db import models

# Create your models here.
class ShowModel(models.Model):
 
    # fields of the model
    name = models.CharField(max_length = 200)
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name