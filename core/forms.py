from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Group, LeetCodeStats

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    leetcode_username = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "leetcode_username")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            LeetCodeStats.objects.create(
                user=user,
                leetcode_username=self.cleaned_data["leetcode_username"]
            )
        return user

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class JoinGroupForm(forms.Form):
    group_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
