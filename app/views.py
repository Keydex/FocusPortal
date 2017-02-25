from django.shortcuts import render

# Create your views here.
def index(request):
	q = request.GET.get('code');
	print(q);
	return render(request, "index.html");
