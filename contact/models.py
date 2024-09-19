from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class ContactUs(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=100, blank=True)


class Practice(BaseModel):
    icons = models.FileField(upload_to='icons/')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)


