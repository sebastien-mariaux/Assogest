from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager

from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # username = None   # This is introducing too many issues, let's keep it for now... :(
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} ({self.email})"
        return self.email



