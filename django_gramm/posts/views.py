from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import CreatePost
from .models import Post, Reaction


class PostsListView(ListView):
    model = Post
    template_name = "posts/posts_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-date")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePost
    template_name = "posts/post_new.html"
    login_url = "/users/login/"
    success_url = reverse_lazy("posts:list")

    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.author = self.request.user
        newpost.save()
        return super().form_valid(form)


class LikePostApiView(View):
    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        reaction, created = Reaction.objects.get_or_create(post=post)
        liked = False
        if request.user in reaction.likes.all():
            reaction.likes.remove(request.user)
        else:
            liked = True
            reaction.likes.add(request.user)
        data = {"liked": liked, "updated_likes_count": reaction.likes.count()}
        return JsonResponse(data)
