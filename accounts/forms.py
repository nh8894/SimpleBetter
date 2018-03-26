from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate

from django import forms


#class LoginForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#
#    class Meta:
#        model = User 
#        fields = ['username', 'password']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, Your username or password does not exist.")
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
