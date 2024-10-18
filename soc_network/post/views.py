from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    is_liked = Like.objects.filter(user=request.user, post=post).exists()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', post_id=post_id)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Отображаем все посты, отсортированные по дате
    return render(request, 'posts/post_list.html', {'posts': posts})





@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Проверка, является ли текущий пользователь создателем поста
    if post.user != request.user:
        return redirect('post_detail', post_id=post.id)  # Или можете добавить сообщение об ошибке

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:
        comment.delete()  # Удаляем комментарий
        # Можно добавить сообщение об успешном удалении, если необходимо
    return redirect('post_detail', post_id=comment.post.id) 