from django.db import models

# Create your models here.
from personn.models.personn import PersonModels

class Teachermodels(PersonModels):
    available = models.BooleanField(default=True)
    specially = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birthday}) - {self.gender} {self.phone_number}  [{self.available}] - {self.specially} "
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'gender': self.gender,
            'phone_number': self.phone_number,
            'url_picture': self.url_picture,
            'available': self.available,
            'specially': self.specially
        }