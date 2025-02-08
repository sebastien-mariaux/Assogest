from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        self.login_url = reverse('login')
        self.organization_list_url = reverse('organization:organization-list')

    def test_login_page_loads(self):
        """Test that the login page loads correctly and uses the proper template"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_successful_login_and_redirect(self):
        """Test that users can login successfully and are redirected to the organization list"""
        login_data = {
            'username': 'test@example.com',
            'password': 'testpass123'
        }

        response = self.client.post(self.login_url, login_data)

        self.assertRedirects(response, self.organization_list_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.wsgi_request.user, self.user)

    def test_failed_login_with_wrong_password(self):
        """Test that login fails with incorrect credentials and shows error message"""
        login_data = {
            'username': 'test@example.com',
            'password': 'wrongpass'
        }

        response = self.client.post(self.login_url, login_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(
            response, "Identifiants incorrects")


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.organization_list_url = reverse('organization:organization-list')

        self.valid_user_data = {
            'email': 'newuser@example.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        }

    def test_registration_page_loads(self):
        """Test that the registration page loads correctly and uses the proper template"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_successful_registration(self):
        """Test that users can register successfully and are redirected to login"""
        response = self.client.post(self.register_url, self.valid_user_data)

        self.assertRedirects(response, self.login_url)
        self.assertTrue(User.objects.filter(
            email=self.valid_user_data['email']).exists())

    def test_registration_with_existing_email(self):
        """Test that registration fails when using an email that already exists"""
        User.objects.create_user(
            username='existinguser',
            email=self.valid_user_data['email'],
            password='TestPass123!'
        )

        response = self.client.post(self.register_url, self.valid_user_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User with this Email already exists.")

    def test_registration_with_mismatched_passwords(self):
        """Test that registration fails when passwords don't match"""
        invalid_data = self.valid_user_data.copy()
        invalid_data['password2'] = 'DifferentPass123!'

        response = self.client.post(self.register_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")

    def test_registration_with_weak_password(self):
        """Test that registration fails when using a weak password"""
        invalid_data = self.valid_user_data.copy()
        invalid_data['password1'] = 'password'
        invalid_data['password2'] = 'password'

        response = self.client.post(self.register_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This password is too common")

    def test_registration_with_missing_fields(self):
        """Test that registration fails when required fields are missing"""
        invalid_data = {
            'email': 'newuser@example.com',
            'password1': 'TestPass123!'
        }

        response = self.client.post(self.register_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # URLs utiles
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')

        self.client.login(username='test@example.com', password='testpass123')

    def test_successful_logout_and_redirect(self):
        """Test that users can logout successfully and are redirected to home"""
        self.assertTrue(self.client.session.get('_auth_user_id'))

        response = self.client.post(self.logout_url)

        self.assertRedirects(response, self.home_url)

        self.assertFalse(self.client.session.get('_auth_user_id'))

    def test_get_request_not_allowed(self):
        """Test that GET requests to logout view are not allowed"""
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 405)
