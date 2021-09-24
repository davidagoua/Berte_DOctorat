from django import forms
from .models import Provider


class ProviderForm(forms.ModelForm):

    x = forms.DateTimeField()
    y = forms.DateTimeField()

    class Meta:
        fields = '__all__'
        model = Provider
