# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Rating(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    rating = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.name.first_name