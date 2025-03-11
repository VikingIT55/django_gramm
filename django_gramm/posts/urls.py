from django.urls import path

from .views import LikePostApiView, PostCreateView, PostsListView

app_name = "posts"

urlpatterns = [
    path("", PostsListView.as_view(), name="list"),
    path("new-post/", PostCreateView.as_view(), name="new-post"),
    path("post-api/<int:post_id>", LikePostApiView.as_view(), name="like-post-api"),
]
