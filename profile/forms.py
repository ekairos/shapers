from django import forms
from allauth.account.forms import SignupForm


class UserSignupForm(SignupForm):
    """Override Allauth signup form"""

    first_name = forms.CharField(
        max_length=40,
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=40,
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    field_order = ['email', 'email2', 'first_name', 'last_name', 'username',
                   'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """Overriding placeholders and required fields"""

        super().__init__(*args, **kwargs)
        self.fields['username'].required = False

        for field in self.fields:
            if self.fields[field].required:
                placeholder = \
                    f'{self.fields[field].widget.attrs["placeholder"]} *'
            else:
                placeholder = \
                    f'{self.fields[field].widget.attrs["placeholder"]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder

    def save(self, request):

        user = super(UserSignupForm, self).save(request)

        return user
