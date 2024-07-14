from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def index(request):
    post = Post.objects.all().order_by('-date_posted')

    context = {
        "post": post,
    }

    return render(request, 'core/index.html', context=context)

@login_required(login_url='login')
def post_detail(request, slug):
    # post = get_object_or_404(Post, slug=slug)

    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=slug)
    else:
        messages.error(request,"You must login to continue!")

    context = {
        "post": post
    }

    return render(request, 'core/post_detail.html', context=context)


def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
        
    context = {
        "form": form
    }

    return render(request, 'core/register.html', context=context)


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'core/login.html', context=context)


def signout(request):
    logout(request)

    return redirect('login')

