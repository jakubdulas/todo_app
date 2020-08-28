from django.db import models

# Create your models here.

class Task(models.Model):
    text = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.text + ' | ' + str(self.complete)