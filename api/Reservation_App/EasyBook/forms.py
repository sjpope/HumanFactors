# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description', 'rating', 'price']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 8}),
        }
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)  

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
