from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import *
class ContactForm(ModelForm):
    class Meta:
        model = contactMessage
        fields = {'name', 'phone_number', 'email', 'message'}

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Full name'}),
            'phone_number': TextInput(attrs={'placeholder': 'Phone number with country code'}),
            'email': EmailInput(attrs={'placeholder': 'Email addess'}),
            'message': Textarea(attrs={'placeholder': 'Your message', 'rows':'5'})
        }