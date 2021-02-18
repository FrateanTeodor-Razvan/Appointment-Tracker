from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=20, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20, widget=forms.TextInput)
    last_name = forms.CharField(max_length=20, widget=forms.TextInput)
    phone_number = forms.CharField(max_length=1, widget=forms.NumberInput, required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
