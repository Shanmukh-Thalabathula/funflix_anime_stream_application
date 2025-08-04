from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from . forms import *

from . models import *


# Create your views here.

# Authentication process here

# User Register
def userRegister(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created successfully! Welcome, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'anime/login_register.html', {'form': form})


# user login
def userLogin(request):
    page = 'login'
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'anime/login_register.html', {'form': form, 'page': page})


# user logout
@login_required(login_url='user-login')
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('user-login')


# template rendering here
@login_required(login_url='user-login')
def home(request):
    fav_list = Favorite.objects.filter(user=request.user).values_list('anime_title_id', flat=True)
    category = request.GET.get('category','')
    search = request.GET.get('search','')
    if search:
        anime_list = AnimeTitle.objects.filter(
            Q(title__icontains=search)
        )
    elif category:
        anime_list = AnimeTitle.objects.filter(
            Q(category__name__icontains=category)
        )
    else:
        anime_list = AnimeTitle.objects.all()

    context = {'anime_list':anime_list,'fav_list':fav_list}
    return render(request,'anime/home.html',context)

# anime episodes
@login_required(login_url='user-login')
def episodes(request,pk):
    anime = AnimeTitle.objects.get(title=pk)
    episodes = anime.episode_set.all
    context = {'episodes':episodes,'anime':anime}
    return render(request,'anime/anime_episodes_list.html',context)

@login_required(login_url='user-login')
def video(request,pk):
    episode = Episode.objects.get(id = pk)
    context = {'episode':episode}
    return render(request,'anime/display.html',context)

@login_required(login_url='user-login')
def fav_list(request):
    search = request.GET.get('search','')
    if search:
        fav_list = Favorite.objects.filter(user=request.user,anime_title__title__icontains=search)
    else:
        fav_list = Favorite.objects.filter(user=request.user)
    context = {'fav_list': fav_list}
    return render(request, 'anime/favorite.html', context)


@login_required(login_url='user-login')
def favorite(request, pk):
    anime = AnimeTitle.objects.get(id=pk)
    anime_fav = Favorite.objects.filter(user=request.user, anime_title=anime).first()

    if anime_fav:
        anime_fav.delete()
        messages.info(request, f'Removed {anime.title} from favorites.')
    else:
        Favorite.objects.create(user=request.user, anime_title=anime)
        messages.success(request, f'Added {anime.title} to favorites!')

    return redirect('fav-list')



@login_required(login_url='user-login')
# Categorise
def category(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'anime/category.html',context)

# project details
def details(request):
    return render(request,'anime/details.html')
