from django import forms

class SearchForm(forms.Form):
   Search = forms.CharField(max_length=200, required=True)
   