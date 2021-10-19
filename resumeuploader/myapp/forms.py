from django import forms
from django.db.models.base import Model
from django import forms
from django.forms import widgets
from .models import Resume

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]

Job_City_Choices=[
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Pune','Pune'),
    ('Banglore','Banglore'),
    ('Dhanbad','Dhanbad')
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=Job_City_Choices,widget=forms.CheckboxSelectMultiple,label='Preffered Job Location')
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','pin','state','email','mobile','job_city','profile_image','my_file']
        Labels={'name':'full name','dob':'Date Of Birth','pin':'Pin Code','mobile':'Mobile No','profile_image':'Profile_Image','my_file':'Document'}       
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control' , 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'Pin':forms.NumberInput(attrs={'class':'form-control'}),
            'State':forms.Select(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),       
        }