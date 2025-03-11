from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=75)
    images = CloudinaryField("images")
    tags = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.tags = " ".join(
            [tag if tag.startswith("#") else "#" + tag for tag in self.tags.split()]
        )
        super(Post, self).save(*args, **kwargs)


class Reaction(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="reaction")
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    unlikes = models.ManyToManyField(User, related_name="post_unlikes", blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def number_of_unlikes(self):
        return self.unlikes.count()
