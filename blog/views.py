from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import PostCreateForm
from .models import Post

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()

        context = {
            'posts':post
        }  

        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm
        context = {
            'form':form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form= PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect("Blog:home")

        context = {    
        }
        return render(request, 'blog_create.html', context)
    
class BlogDetailView(View):
    def get(self, pk, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post':post
        }
        
        return render(request, 'blog_detail.html', context)