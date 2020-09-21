from django.shortcuts import render, HttpResponseRedirect, reverse
from hierarchical.models import Desserts
from hierarchical.forms import AddDessertForm

# Create your views here.


def show_desserts(request):
    return render(request, 'index.html', {'dessert': Desserts.objects.all()})


def add_dessert(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddDessertForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Desserts.objects.create(
                name=data['name'],
                parent=data['parent']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddDessertForm()
    return render(request, html, {'form': form})
