from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
        if request.method == 'POST':
                q = request.POST.get('code')
                t = ['java','python']
                tit = request.POST.get('title')
                post = Post(title=tit, tag=t, code=q)
                post.save()
        content = {"python": Code.objects(category="python"), "java":Code.objects(category="java"), "C":Code.objects(category="c")};
        return render(request, "index.html", content)

def login(request):
        
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
        return render(request, "login.html")
