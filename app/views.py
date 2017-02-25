from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
        if request.method == 'POST':
                q = request.POST.get('code')
                t = ['java','python']
                tit = request.POST.get('title')
                post = Post(title=tit, tag=t, code=q)
                post.save()
        content = ""
        #content = {"python": Code.objects.get(category="python"), "java":Code.objects.get(category="java"), "C":Code.objects.get(category="c")};
        return render(request, "index.html", content)

def login(request):
        return render(request, "login.html")
