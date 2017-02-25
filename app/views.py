from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
        if request.method == 'POST':
                q = request.POST.get('code')
                print(q)
                t = ['java','python']
                tit = request.POST.get('title')
                print(tit)
                post = Post(title=tit, tag=t, code=q)
                print("title: " + post.title + "\ncode: " + post.code)
                post.save()
        return render(request, "index.html")

def output(request):
        for p in Post.objects:
                print p.title
        return render(request, "index.html")
