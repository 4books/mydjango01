from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from app.models import Post


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
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
