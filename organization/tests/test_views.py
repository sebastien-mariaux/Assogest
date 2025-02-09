from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from organization.models import Organization, Membership


class OrganizationAdminViewTest(TestCase):
    def setUp(self):
        # Créer un utilisateur
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )

        # Créer une organisation
        self.organization = Organization.objects.create(
            name='Test Organization',
            slug='test-org'
        )

        # Créer un membership non-admin
        self.membership = Membership.objects.create(
            member=self.user.member,
            organization=self.organization,
            is_admin=False
        )

        # URL de la page admin
        self.admin_url = reverse('organization:organization-admin', kwargs={
                                 'slug': self.organization.slug})

    def test_admin_page_access_denied_for_non_admin(self):
        # Connecter l'utilisateur
        self.client.force_login(self.user)

        # Tenter d'accéder à la page admin
        response = self.client.get(self.admin_url)
        # Vérifier que l'accès est refusé
        self.assertEqual(response.status_code, 403)

    def test_admin_page_access_granted_for_admin(self):
        # Modifier le membership en admin
        self.membership.is_admin = True
        self.membership.save()

        # Connecter l'utilisateur
        self.client.force_login(self.user)
        # Tenter d'accéder à la page admin
        response = self.client.get(self.admin_url)

        # Vérifier que l'accès est autorisé
        self.assertEqual(response.status_code, 200)

    def test_admin_page_access_denied_for_non_member(self):
        # Créer un autre utilisateur qui n'est pas membre
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
        # Connecter l'autre utilisateur
        self.client.force_login(other_user)

        # Tenter d'accéder à la page admin
        response = self.client.get(self.admin_url)

        # Vérifier que l'accès est refusé
        self.assertEqual(response.status_code, 403)
