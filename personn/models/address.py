from django.db import models
class AddressModels(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} {self.street} {self.country}"