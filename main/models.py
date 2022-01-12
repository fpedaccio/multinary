from django.db import models

# Create your models here.

class search_data(models.Model):
    word = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word