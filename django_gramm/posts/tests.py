from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            username="testuser", password="S0m3C0mpl3xP@ssw0rd!"
        )
        cls.test_image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open("test_files/test.jpg", "rb").read(),
            content_type="image/jpeg",
        )
        cls.test_post = Post.objects.create(
            title="Test Post",
            images=cls.test_image,
            tags="test, post",
            author=cls.test_user,
        )
        cls.test_post2 = Post.objects.create(
            title="Test Post 2",
            images=cls.test_image,
            tags="test, post",
            author=cls.test_user,
        )
        cls.test_post3 = Post.objects.create(
            title="Test Post 3",
            images=cls.test_image,
            tags="test, post",
            author=cls.test_user,
        )

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        expected_title = f"{post.title}"
        self.assertEqual(expected_title, "Test Post")

    def test_post_fields(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.tags, "#test, #post")
        self.assertEqual(post.author.username, "testuser")

    def test_post_author_relationship(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author.username, "testuser")

    def test_posts_list_view(self):
        response = self.client.get(reverse("posts:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts_list.html")
        self.assertContains(response, "Test Post")
        self.assertEqual(len(response.context["posts"]), 3)

    def test_post_new_view_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse("posts:new-post"))
        self.assertRedirects(response, "/users/login/?next=/posts/new-post/")

    def test_post_new_view_get_request(self):
        self.client.login(username="testuser", password="S0m3C0mpl3xP@ssw0rd!")
        response = self.client.get(reverse("posts:new-post"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_new.html")

    def test_post_new_view_post_request(self):
        self.client.login(username="testuser", password="S0m3C0mpl3xP@ssw0rd!")
        image = SimpleUploadedFile(
            name="new_test_image.jpg",
            content=open("test_files/test.jpg", "rb").read(),
            content_type="image/jpeg",
        )
        form_data = {
            "title": "New Test Post",
            "tags": "test",
            "images": image,
        }
        response = self.client.post(
            reverse("posts:new-post"), data=form_data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Test Post")
        self.assertTrue(Post.objects.filter(title="New Test Post").exists())
