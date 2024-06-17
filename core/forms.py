from django import forms
from.models import *


class MessageForm(forms.ModelForm):
    # Adding custom attributes to the username field
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name-contact-form-3-ucBtTFGbpH',
        'placeholder': 'Name'

    }))

    # Adding email field with 'required' attribute
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email-contact-form-3-ucBtTFGbpH',
        'placeholder': 'Email'

    }))

    # Adding first_name field with 'required' attribute and max length
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'url-contact-form-3-ucBtTFGbpH',
        'placeholder': 'Phone'

    }))

    # Adding last_name field with 'required' attribute and max length
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'textarea-contact-form-3-ucBtTFGbpH',
        'placeholder': 'Your message here...'
    }))

    class Meta:
        model = Message  # Assuming User is your custom User model
        fields = ('name', 'email', 'phone', 'message')