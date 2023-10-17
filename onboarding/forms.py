from django import forms
from .models import UserInfo, JobInfo, Skills

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class CustomDateInput(forms.DateInput):
    input_type = 'date'

class UserInfo(forms.ModelForm):
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    birthday = forms.DateField(widget=CustomDateInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-xl mt-1 p-3 block w-full rounded-md bg-gray-100 border focus:ring focus:ring-blue-400'
            
    class Meta:
        model = UserInfo
        fields = ('fname', 'lname', 'gender', 'birthday', 'email', 'phone') 
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'John'}),
            'lname': forms.TextInput(attrs={'placeholder': 'Doe'}),
            'email': forms.TextInput(attrs={'placeholder': 'django@hotmail.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+213685748596'}),
        }
        

class JobInfo(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-xl mt-1 p-3 block w-full rounded-md bg-gray-100 border focus:ring focus:ring-blue-400'
            
    class Meta:
        model = JobInfo
        fields = ('job_title', 'years_of_exp', 'main_tech', 'second_tech')
        
class Skills(forms.ModelForm):
    CHOICES = [
        ('yes', 'Yes, I have worked with a team before.'),
        ('no', 'No, i haven\'t worked with a team before.'),
    ]
    team_exp    = forms.ChoiceField(label='Team Experience', choices=CHOICES, required=False, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-xl mt-1 p-3 block w-full rounded-md bg-gray-100 border focus:ring focus:ring-blue-400'
        self.fields['team_exp'].widget.attrs['class'] = 'text-xl text-gray-100'
        
    class Meta:
        model = Skills
        fields = ('soft_skills', 'methodologies', 'team_exp')