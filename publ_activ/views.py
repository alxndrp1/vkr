from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about page')
