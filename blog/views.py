from django.shortcuts import render
from .models import Post


# handles traffic from homepage
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  # we've landed on About page

# Create your views here.
