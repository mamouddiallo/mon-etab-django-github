from django.db import models
from personn.models.personn import PersonModels

class StudentModels(PersonModels):
    mailticket = models.CharField(max_length=100)
    phone_number_label = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age} ans) - {self.classe} {self.mailticket}{self.phone_number_label} {self.phone_number} {self.url_picture} {self.gender} {self.mailticket}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'gender': self.gender,
            'phone_number': self.phone_number,
            'url_picture': self.url_picture,
            'mailticket': self.mailticket,
            'phone_number_label': self.phone_number_label,
            'classe': self.classe
        }