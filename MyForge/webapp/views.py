from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

from .models import Post



def home(request):
    posts = Post.objects.order_by('-published_date')
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'home.html', {'page_obj': page_obj})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})