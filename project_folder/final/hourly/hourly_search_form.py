from django import forms

class HourlySearchForm(forms.Form):
   Search = forms.CharField(max_length=200, required=True)
   