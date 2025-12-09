from django import forms
from .models import ToDo

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your idea, question, or knowledge here...', 'class': 'form-control', 'rows': 5}),
        }
