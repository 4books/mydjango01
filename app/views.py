from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView

from app.forms import PostForm
from app.models import Post


@login_required
def index(request: HttpRequest) -> HttpResponse:
    # if not request.user.is_authenticated:
    #     return redirect("/account/login/")

    qs = Post.objects.all()
    # qs = [
    #     {"id": 1, "title": "post #1"},
    #     {"id": 2, "title": "post #2"},
    # ]
    return render(
        request,
        "app/index.html",
        {
            "post_list": qs,
        },
    )


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )


post_new = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    success_url="/app/",
)
