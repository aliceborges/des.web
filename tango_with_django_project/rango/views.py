#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

# Create your views here.

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	# for c in category_list:
		# print(c.name, c.likes)
		# print(category_list)
	context_dict = {'categories': category_list}

	return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html', {'autor': 'Alice Borges'})