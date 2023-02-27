from django.forms import ModelForm, TextInput, EmailInput, Textarea, ChoiceField, DateField,FileField, DateInput,FileInput
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

class ApplicationForm(ModelForm):
    class Meta:
        model = ApplicationFormModel
        fields = {'firstName', 'lastName', 'idOrPassport','email','telephone'}
                #   'dob','gender','cv','nationalIdOrPassport','workCertificate',
                #   'refereeName','refereeAddress','refereeTelephone','refereeInstitution','refereeOccupation'}
        
        widgets = {
            'firstName': TextInput(attrs={'placeholder': 'First name'}),
            'lastName': TextInput(attrs={'placeholder': 'Last Name'}),
            'idOrPassport': TextInput(attrs={'placeholder': 'ID or Passport'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'telephone': TextInput(attrs={'placeholder': 'Telephone'}),
            # 'dob': DateInput(),
            # 'gender': TextInput(attrs={'placeholder': 'Gender'}),
            # 'cv': FileInput(),
            # 'nationalIdOrPassport': FileInput(),
            # 'workCertificate': FileInput(),
            # 'refereeName': TextInput(attrs={'placeholder': 'Referee Full Name'}),
            # 'refereeAddress': TextInput(attrs={'placeholder': 'Address'}),
            # 'refereeTelephone': TextInput(attrs={'placeholder': 'Telephone'}),
            # 'refereeInstitution': TextInput(attrs={'placeholder': 'Institution'}),
            # 'refereeOccupation': TextInput(attrs={'placeholder': 'Occupation'}),
           
        }
