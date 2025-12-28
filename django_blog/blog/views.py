from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__icontains=tag_name)
    return render(
        request,
        'blog/tag_posts.html',
        {'posts': posts, 'tag': tag_name}
    )


def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()

    return render(
        request,
        'blog/search_results.html',
        {'posts': posts, 'query': query}
    )

