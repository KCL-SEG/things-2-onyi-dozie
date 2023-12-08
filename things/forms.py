"""Forms of the project."""
from .models import Thing
from django import forms

# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta: 
        model = Thing
        fields = ['name','description','quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(attrs={'min':0}),
        }


