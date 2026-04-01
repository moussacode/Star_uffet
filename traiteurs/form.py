from django import forms
from .models import Traiteur
class DevenirTraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = [
            'nomcomplet',
            'specialites',
            'experience',
            'description',
            'adresse',
            'email',
            'telephone',
            'image'
        ]

        # fields = ['__all__']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'experience': forms.NumberInput(attrs={'min': 0}),
            'specialites' : forms.CheckboxSelectMultiple(),
        }