from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=255, initial='')
    last_name = forms.CharField(max_length=255, initial='')
    email = forms.EmailField(initial='')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    invited_by = forms.IntegerField(required=False)



