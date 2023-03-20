from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','input']
        labels = {'input':''}
        widgets = {
            'input':forms.TextInput(attrs={'placeholder':'Ask your question','class':'form-control','style':"margin-left: 10px;"}),
        }
