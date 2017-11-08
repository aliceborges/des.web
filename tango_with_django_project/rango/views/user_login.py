#coding:utf-8
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Sua conta está desabilitada.")
        else:
            msg = "Dados de login inválidos: {0}, {1}".format(username, password)
            print(msg)
            return HttpResponse(msg)
    else:
       return render(request, 'rango/login.html', {})

    def __unicode__(self):
        return '%s' %self.name