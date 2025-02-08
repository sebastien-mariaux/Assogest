from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


def async_send_email(subject,
                     message,
                     from_email=None,
                     recipient_list=None,
                     fail_silently=False,
                     auth_user=None,
                     auth_password=None,
                     connection=None,
                     html_message=None):
    """
    Accepts the same arguments as Django's send_mail function, but sends the email
    asynchronously.
    """
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL

    deliver_email.delay(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=fail_silently,
        auth_user=auth_user,
        auth_password=auth_password,
        html_message=html_message
    )


@shared_task
def deliver_email(subject,
                  message,
                  from_email,
                  recipient_list,
                  fail_silently=False,
                  auth_user=None,
                  auth_password=None,
                  html_message=None):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=fail_silently,
        auth_user=auth_user,
        auth_password=auth_password,
        html_message=html_message
    )
