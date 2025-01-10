from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class Member(models.Model):
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
        Member.objects.create(user=instance)


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
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.member.user.email} - {self.organization.name}'
