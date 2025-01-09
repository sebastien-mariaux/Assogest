from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CalendarEvent(models.Model):
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    start_time = models.DateTimeField(
    )
    end_time = models.DateTimeField(
    )
    location = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    inscription_required = models.BooleanField(
        default=False
    )
    organization = models.ForeignKey(
        'nonprofits.Organization',
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        'nonprofits.Member',
        through='Subscription',
        related_name='subscriptions'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.title} - {self.start_time} - {self.end_time}"


class Subscription(models.Model):
    event = models.ForeignKey(
        CalendarEvent,
        on_delete=models.CASCADE
    )
    member = models.ForeignKey(
        'nonprofits.Member',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
