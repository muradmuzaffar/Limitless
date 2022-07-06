from .models import Contact, Subscribtion
from django import forms


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ad'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Soyad'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Müraciətin mətni'
    }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name',
                  'email', 'message']


class SubscribtionForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'e-poçt ünvanınızı qeyd edin',
        'id': 'gilroy-medium',
        'style': 'overflow: hidden;'

    }))

    class Meta:
        model = Subscribtion
        fields = ['email']
