from .models import dmt
from django import forms

class sony(forms.ModelForm):
   
   class Meta:
      model=dmt
      fields='__all__'
