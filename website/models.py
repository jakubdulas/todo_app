from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text + ' | ' + str(self.complete)