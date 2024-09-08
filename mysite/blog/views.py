from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def homepage(request):
    #connecting models to view in here
    all_objects = Post.new_manager.all()
    return render(request, 'index.html', {'posts':all_objects})


def single_post(request, cur_slug):

    #retrieve slug data from db
    object_where_slug_is_slug = get_object_or_404(Post, slug=cur_slug)

    return render(request, 'single.html', {'post':object_where_slug_is_slug})