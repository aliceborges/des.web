#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

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

def show_category(request, category_name_slug):
    # print(category_name_slug)
    # return render(request, 'rango/category.html', {'category':category_name_slug})

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
