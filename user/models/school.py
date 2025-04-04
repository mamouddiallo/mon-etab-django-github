from django.db import models
from user.models.appsetting import AppSettingmodels

# Create your models here.
class SchoolModels(models.Model):
    name = models.CharField(max_length=255)
    url_logo = models.URLField(blank=True, null=True)
    app_setting = models.OneToOneField(AppSettingmodels, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name