from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

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
        'organization.Organization',
        on_delete=models.CASCADE,
        related_name='events'
    )
    members = models.ManyToManyField(
        'organization.Member',
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


def validate_member_in_organization(member, organization):
    if not organization.members.filter(id=member.id).exists():
        raise ValidationError(
            _("%(member)s is not in %(organization)s"),
            params={'member': member.user.email, 'organization': organization.name},
        )


class Subscription(models.Model):
    event = models.ForeignKey(
        CalendarEvent,
        on_delete=models.CASCADE
    )
    member = models.ForeignKey(
        'organization.Member',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ('event', 'member')

    def clean(self):
        validate_member_in_organization(self.member, self.event.organization)
