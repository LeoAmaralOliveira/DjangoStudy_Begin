from django import forms
from apps.gallery.models import Photography


class PhotographyForms(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published',]
        labels = {
            'description': 'Descrição',
            'photo_date': 'Data de registro',
            'user': 'Usuário',
            'name': 'Nome',
            'label': 'Legenda',
            'category': 'Categoria',
            'photo': 'Foto',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'label': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
