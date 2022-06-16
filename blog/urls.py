import imp
from django.urls import URLPattern, path
from .views import BlogListView, BlogCreateView, BlogDetailView


app_name="Blog"

urlpatterns = [

    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail')

    
]
