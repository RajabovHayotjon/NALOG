from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class RegisterUs(BaseModel):
    user = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

class LoginUs(BaseModel):
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)