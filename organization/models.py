from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from organization.managers import MemberManager


class Member(models.Model):
    objects = MemberManager()

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    organizations = models.ManyToManyField(
        'Organization',
        through='Membership',
    )
    events = models.ManyToManyField(
        'agenda.CalendarEvent',
        through='agenda.Subscription',
    )

    def __str__(self):
        return self.user.username


def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create_member(instance)


post_save.connect(create_member, sender=settings.AUTH_USER_MODEL)


class Organization(models.Model):
    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField(
        max_length=100, unique=True
    )
    members = models.ManyToManyField(
        'Member',
        through='Membership',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    is_admin = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ('member', 'organization')

    def __str__(self):
        return f'{self.member.user.email} - {self.organization.name}'
