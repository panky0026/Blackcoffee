from django.db import models

# Create your models here.
class DashboardData(models.Model):
    Intensity = models.FloatField()
    Likelihood = models.FloatField()
    Relevance = models.FloatField()
    Year = models.IntegerField()
    Country = models.CharField(max_length=255)
    Topics = models.CharField(max_length=255)
    Region = models.CharField(max_length=255)
    City = models.CharField(max_length=255)

    def __str__(self):
        return self.Country