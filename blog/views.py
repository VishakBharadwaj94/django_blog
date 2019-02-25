from django.shortcuts import render
from .models import Post # . means from the current package
# from django.http import HttpResponse (not needed)


def home(request):

	context = {'posts':Post.objects.all()}
	return render(request,'blog/home.html',context)
	#context dictionary has to be passed unlike in flask

def about(request):

	return render(request,'blog/about.html',{'title':'about'})