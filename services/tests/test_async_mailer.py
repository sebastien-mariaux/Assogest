from unittest.mock import patch
from django.test import TestCase, override_settings
from django.core import mail
from services.async_mailer import async_send_email, deliver_email
from django.conf import settings


class AsyncMailerTest(TestCase):
    def setUp(self):
        self.email_data = {
            'subject': 'Test Subject',
            'message': 'Test Message',
            'recipient_list': ['test@example.com'],
        }

    @patch('services.async_mailer.deliver_email.delay')
    def test_async_send_email_calls_delay(self, mock_delay):
        async_send_email(**self.email_data)

        mock_delay.assert_called_once_with(
            subject=self.email_data['subject'],
            message=self.email_data['message'],
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=self.email_data['recipient_list'],
            fail_silently=False,
            auth_user=None,
            auth_password=None,
            html_message=None
        )

    def test_deliver_email_sends_email(self):
        deliver_email(
            subject=self.email_data['subject'],
            message=self.email_data['message'],
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=self.email_data['recipient_list']
        )

        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]

        self.assertEqual(sent_mail.subject, self.email_data['subject'])
        self.assertEqual(sent_mail.body, self.email_data['message'])
        self.assertEqual(sent_mail.from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(sent_mail.to, self.email_data['recipient_list'])