from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from ..forms import CategoryForm

@login_required()
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            print(cat, cat.slug)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})
