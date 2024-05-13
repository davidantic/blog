from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm, UpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Post

@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'main/home.html', {"posts": posts})

# - Create a Post

@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    
    return render(request, 'post/create_post_form.html', {"form":form})

# - Update a Post

@login_required(login_url='/login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form  = UpdateForm(instance=post)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request, 'post/update_post_form.html', {"form":form})

# - View/Read a single Post

@login_required(login_url='/login')
def view_post(request, pk):
    all_posts = Post.objects.get(id=pk)

    return render(request, 'post/view_post.html', {"post":all_posts})
 

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form":form})


