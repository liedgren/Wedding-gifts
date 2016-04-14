from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'john@doe.com'}))
    payPal = forms.EmailField(label='PayPal Account', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'john@doe.com'}))
    fullName = forms.CharField(label='Full Name', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))

class LoginForm(forms.Form):
	companyName = forms.CharField(label='Company name', required=False)
	password = forms.CharField(label='Password', required=False, widget=forms.PasswordInput)