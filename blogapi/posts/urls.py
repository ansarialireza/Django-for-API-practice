from django.urls import include, path

from .views import PostList, PostDetail

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    path("api-auth/", include("rest_framework.urls")),
]
