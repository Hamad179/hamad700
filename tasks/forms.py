from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['العنوان', 'الوصف', 'مكتملة', 'الصورة']
        widgets = {
            'العنوان': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اكتب عنوان المهمة'}),
            'الوصف': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'اكتب وصف المهمة'}),
            'مكتملة': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
           'الصورة': forms.ClearableFileInput(attrs={'class': 'form-control-file'})

        }
