from django import forms
from .models import *


class ContactFORM(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'phone_number', 'message']
        widgets = {
            'fullname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your fullname',
                    'onfocus': "this.placeholder = ''",
                    'onblur': "this.placeholder = 'Enter your fullname'",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email address',
                    'onfocus': "this.placeholder = ''",
                    'onblur': "this.placeholder = 'Enter email address'"
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Number',
                    'onfocus': "this.placeholder = ''",
                    'onblur': "this.placeholder = 'Enter Subject'"
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Message',
                    'onfocus': "this.placeholder = ''",
                    'onblur': "this.placeholder = 'Enter Message'",
                    'rows': '1',
                }
            )
        }
