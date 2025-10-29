from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Posts,Interested


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        

class Reguser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']


class Postform(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']

        

class Interestedform(forms.ModelForm):
    class Meta:
        model = Interested
        exclude = ['sender', 'receiver', 'ad']  
