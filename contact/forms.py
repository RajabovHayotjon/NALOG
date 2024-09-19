from django import forms

from .models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email address',
        })

        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Write your subject',
            'cols': 30,
            'rows': 10,
        })
