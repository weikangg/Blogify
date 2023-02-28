from django.urls import path

from . import views
urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("posts", views.AllPostsView.as_view(), name = "posts-page"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(), name="post-detail-page") 
    # Concept of this is slug /posts/my-first-post, more search engine friendly compared to id, 
    # slug checks if it's slug format, string and numbers
]
