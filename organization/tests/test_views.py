from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from organization.models import Organization, Membership


class OrganizationDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.organization = Organization.objects.create(
            name='Test Organization',
            slug='test-org'
        )
        self.membership = Membership.objects.create(
            member=self.user.member,
            organization=self.organization,
            is_admin=True
        )

        self.client.force_login(self.user)

    def test_organization_detail_view(self):
        """
        Test that the organization detail view returns a 200 status code
        and uses the correct template
        """
        response = self.client.get(reverse('organization:organization-detail', kwargs={
            'slug': self.organization.slug
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'organization/organization_detail.html')
        self.assertContains(response, self.organization.name)


class OrganizationAdminViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )

        self.organization = Organization.objects.create(
            name='Test Organization',
            slug='test-org'
        )

        self.membership = Membership.objects.create(
            member=self.user.member,
            organization=self.organization,
            is_admin=False
        )

        self.admin_url = reverse('organization:organization-admin', kwargs={
                                 'slug': self.organization.slug})

    def test_admin_page_access_denied_for_non_admin(self):
        """
        Test that the admin page is denied for non-admin users
        """
        self.client.force_login(self.user)

        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 403)

    def test_admin_page_access_granted_for_admin(self):
        """
        Test that the admin page is granted for admin users
        """
        self.membership.is_admin = True
        self.membership.save()

        self.client.force_login(self.user)
        response = self.client.get(self.admin_url)

        self.assertEqual(response.status_code, 200)

    def test_admin_page_access_denied_for_non_member(self):
        """
        Test that the admin page is denied for non-member users
        """
        other_user = get_user_model().objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        other_organization = Organization.objects.create(
            name='Other Organization',
            slug='other-org'
        )
        Membership.objects.create(
            member=other_user.member,
            organization=other_organization,
            is_admin=True
        )
        self.client.force_login(other_user)

        response = self.client.get(self.admin_url)

        self.assertEqual(response.status_code, 403)
