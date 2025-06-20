from django import forms
from .models import study1

class sform(forms.ModelForm):
    class Meta:
        model = study1
        fields = '__all__'