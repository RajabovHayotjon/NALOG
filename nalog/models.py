from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Directors(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField()


class home_contact(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()


