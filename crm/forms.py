from django import forms

class UserRegisterForm(forms.Form):

    username = forms.CharField(max_length=30)

    password = forms.CharField(max_length=10)