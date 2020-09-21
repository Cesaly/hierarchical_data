from django import forms
from hierarchical.models import Desserts
from mptt.forms import TreeNodeChoiceField


class AddDessertForm(forms.Form):
    name = forms.CharField(max_length=48)
    parent = TreeNodeChoiceField(queryset=Desserts.objects.all())
