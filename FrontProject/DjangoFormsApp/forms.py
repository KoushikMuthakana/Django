from django import forms
from django.core import validators
from .models import User

# Custom Validation
def check_start_z(value):
    print(value)
    if value[0].lower != 'z':
        raise forms.ValidationError("Make sure start with z")
    
    

class FormData(forms.Form):

    name=forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control',
         
    }))
    email=forms.EmailField()
    verify_email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    # validator for single field
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError('Bot has cached..!!')
        return botcatcher
    
     #Validator for entire form
     
    def clean(self):
        all_cleaned_data=super().clean()
        email=all_cleaned_data['email']
        verify_email=all_cleaned_data['verify_email']
        if email!= verify_email:
            raise forms.ValidationError("Email ID should be same..!!")



# Form using the Model and Storing the form Data into models

class UserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields="__all__"



    

