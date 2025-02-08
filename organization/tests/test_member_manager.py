from django.test import TestCase
from unittest.mock import patch
from django.db.models.signals import post_save
from organization.models import Member, create_member
from django.contrib.auth import get_user_model

User = get_user_model()


class MemberManagerTest(TestCase):
    """Test suite for the Member model manager"""

    def setUp(self):
        post_save.disconnect(create_member, sender=User)
        self.user = User.objects.create_user(
            username='newmember@test.com',
            email='newmember@test.com',
            password='testpass123'
        )

    def tearDown(self):
        post_save.connect(create_member, sender=User)

    @patch('organization.managers.async_send_email')
    def test_create_member_sends_email(self, mock_async_send_email):
        """Test that creating a member through the manager sends a welcome email to the user"""
        Member.objects.create_member(self.user)

        mock_async_send_email.assert_called_once()
        call_kwargs = mock_async_send_email.call_args.kwargs
        self.assertEqual(call_kwargs['recipient_list'], [self.user.email])
