from django.db import models
class AppSettingmodels(models.Model):
    smtp_server = models.CharField(max_length=100)
    smtp_port = models.IntegerField()
    smtp_username = models.CharField(max_length=100)
    smtp_password = models.CharField(max_length=100)
    