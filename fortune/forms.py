from django import forms

class UserForm(forms.Form):
	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder': 'Enter your Username'}))