#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from ..forms import PageForm
from ..models import Category

@login_required()
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
        print(category.name)
    except Category.DoesNotExist:
        category = None
        print(category_name_slug, 'não existe')
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return HttpResponseRedirect(reverse('show_category', kwargs={'category_name_slug':category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)


    def __unicode__(self):
        return '%s' % self.name