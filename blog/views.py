from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post': post})


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

    def post(self, request):
        # do something
        return redirect(detail)
