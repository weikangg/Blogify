from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post


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

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all() # self.object gives us the instance of that particular post.
        return context
    

def post_detail(request, slug):
    identified_post = get_object_or_404(Post,slug=slug)
    return render(request,'blog/post-detail.html', {
        'post' : identified_post,
        "post_tags": identified_post.tags.all() # pass in all the tags
    })