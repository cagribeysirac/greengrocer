from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model that extends the default Django user model."""

    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
