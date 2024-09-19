from django import forms
from .models import LoginUs, RegisterUs



class RegisterUSForm(forms.ModelForm):
    class Meta:
        model = RegisterUs
        fields = ('user', 'password', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterUSForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'UserName',
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
        })


class LoginUSForm(forms.ModelForm):
    class Meta:
        model = LoginUs
        fields = ('user', 'password',)

    def __init__(self, *args, **kwargs):
        super(LoginUSForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'UserName',

        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
        })