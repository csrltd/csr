from django.forms import ModelForm, TextInput, EmailInput, Textarea, ChoiceField
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = contactMessage
        fields = {'name', 'phone_number', 'email', 'message'}

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Full name'}),
            'phone_number': TextInput(attrs={'placeholder': 'Phone number with country code'}),
            'email': EmailInput(attrs={'placeholder': 'Email address'}),
            'message': Textarea(attrs={'placeholder': 'Your message', 'rows':'5'})
        }

# class AuthorsForm(ModelForm):

#     # departments = 
#     class Meta:
#         model = authorsForm
#         fields = {'name', 'email', 'department'}

#         widgets = {
#             'name': TextInput(attrs={'placeholder': "Author's name"}),
#             'email': EmailInput(attrs={'placeholder':"author@abc.com"}),
#             'department': ChoiceField(choices= 'departments')

#         }