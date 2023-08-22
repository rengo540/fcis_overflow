from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from utils.utils import get_id_from_email
import datetime
majors = [
    ('general','General'),
    ('is','IS'),
    ('cs','CS'),
    ('sc','SC'),
    ('sys','SYS'),
    
]




class UserForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model= User 
        fields=['username','first_name','last_name','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].unique = True

        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            college_id = get_id_from_email(email)
            

            if college_id is None :
                raise forms.ValidationError('that is not an college email, must have an id ')
            else :
                if not len(college_id)==11:
                    raise forms.ValidationError('college id is not complete')

                year = college_id[:4]
                if int(year)> datetime.datetime.now().year :
                    raise forms.ValidationError('invalid college id')

            if not email.endswith('@cis.asu.edu.eg'):
                raise forms.ValidationError('Email must be end with @cis.asu.edu.eg')
        return email