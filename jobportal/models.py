from django.db import models
from django.urls import reverse


# Create your models here.
class UserInfo(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    challenged = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('login', args=[str(self.email)])

    def __str__(self):
        return str(self.email)


class PsyForm(models.Model):
    details = models.ForeignKey(UserInfo, on_delete=True)
    field1 = models.CharField(max_length=20)
    field2 = models.CharField(max_length=20)
    field3 = models.CharField(max_length=20)
    field4 = models.CharField(max_length=20)

    def __str__(self):
        return str(self.details)
