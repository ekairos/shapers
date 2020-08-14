from django import forms
from allauth.account.forms import SignupForm, LoginForm


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

    field_order = ['email', 'email2', 'username', 'first_name', 'last_name',
                   'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].required = False
        self.fields['last_name'].required = False

        for field in self.fields:
            if self.fields[field].required:
                placeholder = \
                    f'{self.fields[field].widget.attrs["placeholder"]} *'
            else:
                placeholder = \
                    f'{self.fields[field].widget.attrs["placeholder"]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control ' \
                                                       'col-12 col-md-6 ' \
                                                       'rounded-0'
            self.fields[field].label = False

    def save(self, request):

        user = super(UserSignupForm, self).save(request)

        return user


class UserLoginForm(LoginForm):
    """Overriding forms field class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['placeholder'] = 'Email *'
        self.fields['password'].widget.attrs['placeholder'] = 'Password *'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control col-12 ' \
                                                       'col-md-6 rounded-0'
            if field == 'remember':
                self.fields[field].widget.attrs['class'] = 'form-check-input'

    def login(self, *args, **kwargs):

        return super(UserLoginForm, self).login(*args, **kwargs)
