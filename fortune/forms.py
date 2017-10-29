from django import forms

class UserForm(forms.Form):
	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder': 'Enter your Username'}))

	def clean_username(self):
		data = self.cleaned_data['username']
		return data