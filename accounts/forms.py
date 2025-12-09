from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name', 'username')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('profile_image', 'username', 'name', 'age', 'bio', 'email', 'standard',
                  'division', 'house', 'stream', 'school')
        widgets = {
            'profile_image': forms.TextInput(attrs={'placeholder': 'Profile Image URL', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Bio', 'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'standard': forms.NumberInput(attrs={'placeholder': 'Standard', 'class': 'form-control'}),
            'division': forms.TextInput(attrs={'placeholder': 'Division', 'class': 'form-control'}),
            'house': forms.TextInput(attrs={'placeholder': 'House', 'class': 'form-control'}),
            'stream': forms.TextInput(attrs={'placeholder': 'Stream', 'class': 'form-control'}),
            'school': forms.TextInput(attrs={'placeholder': 'School', 'class': 'form-control'}),
        }
