from django.urls import path

from . import views
urlpatterns = [
    path("", views.starting_page, name = "starting-page"),
    path("posts", views.posts, name = "posts-page"),
    path("posts/<slug:slug>",views.post_detail, name="post-detail-page") 
    # Concept of this is slug /posts/my-first-post, more search engine friendly compared to id, 
    # slug checks if it's slug format, string and numbers
]
