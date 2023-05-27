from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__():
        return f"{user.first_name} {user.last_name}"

# Model for garbage instance
class Garbage(models.Model):
    id_number = models.IntegerField()
    location = models.CharField(max_length=100)

class LocalGarbage(models.Model):
    id_number = models.IntegerField()
    location = models.CharField(max_length=100)
    level = models.IntegerField(
            default=1,
            validators=[
                MaxValueValidator(100),
                MinValueValidator(0)
                ]
            )
    
