from django.shortcuts import render, redirect, HttpResponse


def index(request):
	context = {
		'hello' : 'Hello World!'
	}
	return render(request, 'hater_app/index.html', context)
