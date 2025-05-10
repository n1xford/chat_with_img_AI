from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PromptForm(forms.Form):
    prompt = forms.CharField(label="Enter your prompt: ",
                             max_length=500,
                             widget=forms.Textarea)

# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]