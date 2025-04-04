from django.db import models
from student.models.student import StudentModels

class AbsenceModels(models.Model):
    absence_date = models.DateField()
    absence_number = models.IntegerField()
    student = models.ForeignKey(StudentModels, on_delete=models.CASCADE)