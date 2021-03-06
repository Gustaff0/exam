from django import forms
from django.forms import widgets

class RegForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Name')
    mail = forms.EmailField(max_length=40, required=True, label='Mail')
    text = forms.CharField(max_length=3000, required=True, label='Text',widget=widgets.Textarea)

