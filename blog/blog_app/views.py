from django.shortcuts import render
from blog_app.models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, template_name="post_list.html", context=context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()
    context = {
        "post": post, 
        "comments":comments
        }
    return render(request, template_name="post_detail.html", context=context)