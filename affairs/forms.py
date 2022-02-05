from django import forms

from .models import Students


class Form(forms.Form):
    name = forms.CharField(max_length=20, label='Name')
    track = forms.CharField(max_length=20, label='Track')

    class Meta:
        model = Students
        fields = '__all__'


class ModelForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label='Name')
    track = forms.CharField(max_length=20, label="Track")

    class Meta:
        model = Students
        fields = '__all__'
