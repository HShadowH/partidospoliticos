from django.db import models

# Create your models here.
from django.db import models

class PoliticalParty(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name
