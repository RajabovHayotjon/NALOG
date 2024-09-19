from django import forms
from .models import home_contact


class QueueForm(forms.ModelForm):
    class Meta:
        model = home_contact
        fields = ('name', 'email', 'date')

    def __init__(self, *args, **kwargs):
        super(QueueForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите дату',
            # 'autofocus': 'autofocus',
        })
