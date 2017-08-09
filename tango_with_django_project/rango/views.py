#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	pagina = '''
	Rango diz olá <br>
	<a href='/rango/about'>Sobre a página</a>
	''';
	return HttpResponse(pagina);

def about(request):
	pagina = '''
	Sobre a página. <br>
	<a href='/rango/'>Retornar a página principal </a>
	''';
	return HttpResponse(pagina);