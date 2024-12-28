from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
        )
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
