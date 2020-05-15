from django.shortcuts import render


def home(request):
	return render(request, 'act/home.html')