from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.
class CustomUser(AbstractUser):
    age= models.PositiveBigIntegerField(null=True, blank=True)
    birthday= models.DateField(default=date.today)