from .models import *
from django.shortcuts import render

# create retriever_function
def retriever_function(request):
    all_posts_response = Post.objects.order_by('-created_at')
    return render(request, 'news.html', context={'app_response': all_posts_response})


# create detail_function
def detail_function(request, id):
    news_post = Post.objects.get(id=id)
    return render(request, 'news_post.html', context={'post': news_post})