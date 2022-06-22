import imp
from django.urls import URLPattern, path
from .views import (
    BlogDeleteView,
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)


app_name = "Blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="delete"),
]
