from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Organization(models.Model):
    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField(
        max_length=100, unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    users = models.ManyToManyField(
        User,
        through='UserOrganization',
        related_name='user_organizations'
    )

    def __str__(self):
        return self.name


class UserOrganization(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.user.email} - {self.organization.name}'


class User(AbstractUser):
    email = models.EmailField(
        unique=True
    )
    # remove username field
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    updated_at = models.DateTimeField(
        auto_now=True
    )
    organizations = models.ManyToManyField(
        'core.Organization',
        through=UserOrganization,
        related_name='user_organizations'
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} ({self.email})"
        return self.email
