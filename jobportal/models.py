from django.db import models
from django.urls import reverse
# Create your models here.
class UserInfo(models.Model):

    email = models.EmailField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('login', args=[str(self.email)])

    def __str__(self):
        return str(self.email)