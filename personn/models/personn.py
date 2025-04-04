from django.db import models
from .address import AddressModels
from user.models.user import UserModels
import datetime 
class Gender(models.TextChoices):
    MEN = 'MEN', 'Men'
    WOMEN = 'WOMEN', 'Women'
    OTHER = 'OTHER', 'Other'

class PersonModels(models.Model):
    birthday = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    url_picture = models.URLField()
    gender = models.CharField(max_length=10, choices=Gender.choices)
    address = models.OneToOneField(AddressModels, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(UserModels, on_delete=models.CASCADE, null=True)
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birthday}) - {self.gender} {self.phone_number} "    
