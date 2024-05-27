from django import forms

from .models import Observation
  
class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['date', 'min_f', 'max_f', 'uv', 'notes']
        widgets = {
        }