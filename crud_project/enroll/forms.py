from django import forms
from .models import student
from django.core import validators


class studentregisration(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'password']

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': "form-control"}),
        #     'email': forms.EmailField(attrs={'class': "form-control"}),
        #     'password': forms.PasswordInput(attrs={"class": 'form-control'}),
        # }
