from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from social_django.models import UserSocialAuth
from unittest.mock import patch


class SocialAuthGoogle(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="S0m3C0mpl3xP@ssw0rd!"
        )
        self.social_auth = UserSocialAuth.objects.create(
            user=self.user, provider="google-oauth2", uid="123456789"
        )
        self.client = Client()

    @patch("social_core.backends.google.GoogleOAuth2.auth_complete")
    def test_social_auth_login_success(self, mock_auth_complete):
        setattr(self.user, "social_user", self.social_auth)
        mock_auth_complete.return_value = self.user
        url = reverse("social:complete", args=["google-oauth2"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user.username, "testuser")

    @patch("social_core.backends.google.GoogleOAuth2.auth_complete")
    def test_social_auth_login_failure(self, mock_auth_complete):
        mock_auth_complete.return_value = None
        url = reverse("social:complete", args=["google-oauth2"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)


class SocialAuthGithub(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="S0m3C0mpl3xP@ssw0rd!"
        )
        self.social_auth = UserSocialAuth.objects.create(
            user=self.user, provider="github", uid="987654321"
        )
        self.client = Client()

    @patch("social_core.backends.github.GithubOAuth2.auth_complete")
    def test_social_auth_login_success_github(self, mock_auth_complete):
        setattr(self.user, "social_user", self.social_auth)
        mock_auth_complete.return_value = self.user
        url = reverse("social:complete", args=["github"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user.username, "testuser")

    @patch("social_core.backends.github.GithubOAuth2.auth_complete")
    def test_social_auth_login_failure_github(self, mock_auth_complete):
        mock_auth_complete.return_value = None
        url = reverse("social:complete", args=["github"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)
