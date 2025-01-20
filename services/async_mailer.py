from time import sleep

from celery import shared_task
from django.core.mail import send_mail


def async_send_email(*args, **kwargs):
    """
    Accepts the same arguments as Django's send_mail function, but sends the email asynchronously.
    """
    deliver_email.apply_async(args=args, kwargs=kwargs)


@shared_task()
def deliver_email(*args, **kwargs):
    send_mail(*args, **kwargs)
