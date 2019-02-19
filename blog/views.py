from django.shortcuts import render
# from django.http import HttpResponse (not needed)

posts = [

	{

		'author':'Corey MS',
		'title':'Blog Post 1',
		'content':'content 1',
		'date':'Aug 2018'

	},
	{

		'author':'Corey MS2',
		'title':'Blog Post 2',
		'content':'content 2',
		'date':'Aug 2019'

	}

]

def home(request):

	context = {'posts':posts}
	return render(request,'blog/home.html',context)
	#context dictionary has to be passed unlike in flask

def about(request):

	return render(request,'blog/about.html',{'title':'about'})