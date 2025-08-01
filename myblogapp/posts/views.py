from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Post

def index(request):
  #return HttpResponse("Hello World! このページは投稿のインデックスです。")
  posts = Post.objects.order_by('-published')
  return render(request,'posts/index.html',{'posts':posts})

def post_detail(request,post_id):
  post = get_object_or_404(Post,pk=post_id)
  return render(request,'posts/post_detail.html',{'post':post})

"""
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("そのようなページはありません")

    return render(request, 'posts/post_detail.html', {'post': post})
"""

# Create your views here.
