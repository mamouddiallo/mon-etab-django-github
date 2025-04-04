from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from user.models.school import SchoolModels

class CustomUserManager(BaseUserManager):
    def create_user(self, pseudo, password, **extra_fields):
        if not pseudo:
            raise ValueError("Le pseudo est obligatoire")
        if not password:
            raise ValueError("Le mot de passe est obligatoire")

        extra_fields.setdefault('is_active', True)

        user = self.model(pseudo=pseudo, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pseudo, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(pseudo, password, **extra_fields)

class UserModels(AbstractBaseUser, PermissionsMixin):
    pseudo = models.CharField(max_length=50, unique=True)
    creation_date = models.DateField(auto_now_add=True)
    school=models.ForeignKey(SchoolModels, on_delete=models.SET_NULL, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'pseudo'  
    REQUIRED_FIELDS = ['password']  

    
    def __str__(self):
        return self.pseudo , self.creation_date
    
    def to_dict(self):
        return {
            'pseudo': self.pseudo,
            'creation_date': self.creation_date,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
        }
