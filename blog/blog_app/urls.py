from django.urls import path
from blog_app.views import post_detail, post_list

urlpatterns = [
    path("", post_list, name="post-list"),
    path("post/<int:post_id>", post_detail, name="post-detail")

]