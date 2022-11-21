from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(min_length=8, max_length=100, required=True)
    login = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), required=True)


class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, label="Login", required=True)
    password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput(), required=True)
    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label="Remember for 7 days")
