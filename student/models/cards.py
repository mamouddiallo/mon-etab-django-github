from django.db import models
from student.models.student import StudentModels

class StudentCardsModels(models.Model):
    reference = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    student = models.ForeignKey(StudentModels, on_delete=models.CASCADE)