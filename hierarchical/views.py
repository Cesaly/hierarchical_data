from django.shortcuts import render, HttpResponseRedirect, reverse
from hierarchical.models import Genre
from hierarchical.forms import AddFilesForm

# Create your views here.


def show_files(request):
    return render(request, 'index.html', {'files': Genre.objects.all()})


def add_files(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddFilesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Genre.objects.create(
                name=data['name'],
                parent=data['parent']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddFilesForm()
    return render(request, html, {'form': form})
