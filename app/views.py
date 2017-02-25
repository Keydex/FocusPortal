from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
        if request.method == 'POST':
                q = request.POST.get('code')
		print q
                t = ['java','python']
                tit = request.POST.get('title')
		print tit
                post = Post(title=tit, tag=t, code=q)
                post.save()
        #content = {"python": Code.objects.get(category="python"), "java":Code.objects.get(category="java"), "C":Code.objects.get(category="c")};
        return render(request, "index.html")

def login(request):
        return render(request, "login.html")
