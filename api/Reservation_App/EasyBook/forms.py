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
        email = self.cleaned_data.get('email')  # Use get to avoid KeyError if email is not provided
        if email:  # Check if email is not empty
            email = email.lower()  # Normalize the email by making it lowercase
            if User.objects.filter(email=email).exists():  # Check if email already exists in the database
                raise ValidationError("Email already exists")
        return email
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
