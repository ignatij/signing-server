from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(label='Password', widget=forms.PasswordInput,max_length=100, min_length=4)
	confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, max_length=100, min_length=4)
	email = forms.EmailField()

	def clean(self):
		data = self.cleaned_data
		username = data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("Username already exists!")

		password = data['password']
		confirm_password = data['confirm_password']
		if password != confirm_password:
			raise forms.ValidationError("Passwords do not match!")

	
class UploadFileForm(forms.Form):
	file = forms.FileField()
