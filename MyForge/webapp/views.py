from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

from .models import Post



def home(request):
    posts = Post.objects.filter(is_listed=True).order_by("-published_date")
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'home.html', {'page_obj': page_obj})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})

def dpm(request):
    post = get_object_or_404(Post, slug="data-product-management")
    return render(request, 'dpm.html', {'post': post})

def datagovernance(request):
  post = get_object_or_404(Post, slug="data-governance")
  return render(request, 'datagovernance.html', {'post': post})
