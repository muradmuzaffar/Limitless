from .models import Contact
from django import forms


MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Surname'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Message'
    }))
    complain_type = forms.ChoiceField(choices=MY_CHOICES
                                      )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name',
                  'email', 'message', 'complain_type']
