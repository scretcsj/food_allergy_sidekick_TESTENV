from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    allergies = forms.MultipleChoiceField(
        choices=UserProfile.ALLERGY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'allergies')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['allergies']
