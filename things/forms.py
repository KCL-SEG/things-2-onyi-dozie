"""Forms of the project."""
from .models import Thing
from django import forms

# Create your forms here.

class ThingForm(forms.Form):
    class Meta: 
        model = Thing
        exclude = ['created_at']
        fields = ['name','description','quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(attrs={'min':0}),
        }


