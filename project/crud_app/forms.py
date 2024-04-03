from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.PasswordInput(attrs={'class':'form-control'}),
            'dob': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'course': forms.Select(attrs={'class':'form-control'}),
            'fees': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={
            'dob':"Date Of Birth"
        }