from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Credits(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    credit = models.IntegerField(null=True, default=1000)

    def __str__(self):
        return self.name.first_name