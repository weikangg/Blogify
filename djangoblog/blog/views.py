from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import CommentForm

# Create your views here.

# Class based view for starting page.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts" # default is object_list

    def get_queryset(self):
        query =  super().get_queryset()
        data = query[:3]
        return data

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # does not support negative indicing.
    return render(request,"blog/index.html", {
        "posts": latest_posts
    })

# Class based view for all posts page.

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request,'blog/all-posts.html', {
        "all_posts": all_posts
    })

# Class based view for individual post view.

class SinglePostView(View):

    def get(self,request, slug):
        post = Post.objects.get(slug=slug) # slug will be received as part of the url.
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self,request, slug):  # slug will also be received here since we made a post request to the url with the slug in the form itself in post-detail.html.
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # don't hit the database first yet. we need to append which post this comment was for first
            comment.post = post # attach that particular post to the comment
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args = [slug])) # i want to reload to this particular page using the get request.
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request,"blog/post-detail.html", context)

def post_detail(request, slug):
    identified_post = get_object_or_404(Post,slug=slug)
    return render(request,'blog/post-detail.html', {
        'post' : identified_post,
        "post_tags": identified_post.tags.all() # pass in all the tags
    })