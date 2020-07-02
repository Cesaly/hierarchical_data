from django import forms
from hierarchical import Genre
from mptt.forms import TreeNodeChoiceField


class AddFilesForm(forms.Form):
    name = forms.CharField(max_length=48)
    parent = TreeNodeChoiceField(quertset=Genre.objects.all())
