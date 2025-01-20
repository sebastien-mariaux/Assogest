from django.db import models
from services.async_mailer import async_send_email


class MemberManager(models.Manager):
    def create_member(self, user):
        member = self.create(user=user)
        self.__notify_user(user)
        return member

    @staticmethod
    def __notify_user(user):
        async_send_email(
            'Welcome to our platform',
            'Thanks for signing up!',
            recipient_list=[user.email]
        )
