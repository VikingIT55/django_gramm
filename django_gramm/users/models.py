from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avatar = CloudinaryField(
        "avatar",
        default="https://res.cloudinary.com/dn1lqn2zp/image/upload/v1724937965/default_c0yccz.jpg",
    )
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def number_of_followers(self):
        return Subscription.objects.filter(following=self.user).count()

    def number_of_following(self):
        return Subscription.objects.filter(follower=self.user).count()


class Subscription(models.Model):
    follower = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
