from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from .forms import PostForm

# Create your views here.
def index(request):
        if request.method == 'POST':
                form = PostForm(request.POST.get('title'), request.POST.get('category'), request.FILES)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.id = 10
                        post.date = timezone.now()
                        post.save()
                        return redirect("homepage")
        else:
                post = PostForm()
        return render(request, "index.html", {'post':post})

def login(request):
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
        return render(request, "login.html")

def test(request):
        return render(request, "test.html")
