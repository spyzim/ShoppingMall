from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import PostForm

# Create your views here.

# 게시판 화면
def posts(request):
    posts = Review.objects.all().order_by("-id")
    
    context = { 'posts' : posts }
    return render(request, 'posts/posts.html', context)

# 리뷰 작석 (Create)
def post_create(request):
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('posts:posts')

    form = PostForm()
    context = { 'form' : form }
    return render(request, 'posts/post_create.html', context)


# 리뷰 읽기 (Read)
def post(request, pk):

    return

# 리뷰 수정 (Update)
def post_update(request, pk):
    post = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    
    form = PostForm(instance=post)
    context = {'form' : form, 'post' : post }
    return render(request, 'posts/post_update.html', context)

# 리뷰 삭제 (Delete)
def post_delete(request, pk):
    post = get_object_or_404(Review, pk=pk)
    post.delete()
    return redirect('posts:posts')

# 썸네일의 원본 사진 보기
def photo_show(request, pk):
    post = get_object_or_404(Review, pk=pk)

    context = { 'post' : post }
    return render(request, 'posts/photo_show.html', context)

def cushion_delete(request, pk):
    post = get_object_or_404(Review, pk=pk)
    context = { 'post' : post }
    return render(request, 'posts/cushion_delete.html', context)