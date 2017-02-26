from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from .models import *
from django.core.files.storage import FileSystemStorage
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                        post = form.save()
                        post.author = request.user.username
                        print request.user.username
                        post.date = timezone.now()
                        post.url = post.code.url
                        post.save()
                        return redirect("homepage")
        else:
                post = PostForm()
        return render(request, "index.html", {'post':post, 'user':request.user})

def login_view(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
                login(request, user)
                return HttpResponseRedirect("homepage")
        else:
                return HttpResponseBadRequest("Login error")
        """
        if request.method == 'POST':
                user = authenticate(username=request.POST.username, password=request.POST.password)
        if user is not None:
                if user.is_active:
                        instance.user = request.user;
                        return HttpResponseRedirect(instance.get_absolute_url())
                else:
                        return Http404("User doesn't exit")
        else:
                return HttpResponse("Wrong username or password")
        """
def logout_view(request):
    logout(request)
    return redirect(login)
    # Redirect to a success page.

def test(request):
        return render(request, "test.html")
