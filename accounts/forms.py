from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_field_attributes('username', _('Username'))
        self.set_field_attributes('first_name', _('First Name'))
        self.set_field_attributes('last_name', _('Last Name'))
        self.set_field_attributes('email', _('Email'))
        self.set_field_attributes('address', _('Address'))
        self.set_field_attributes('city', _('City'))
        self.set_field_attributes('country', _('Country'))
        self.set_field_attributes('zip_code', _('Zip Code'))
        self.set_field_attributes('phone_number', _('Phone Number'))
        self.set_field_attributes('password1', _('Enter Your Password'))
        self.set_field_attributes('password2', _('Confirm Your Password'))

    def set_field_attributes(self, field_name, placeholder):
        self.fields[field_name].widget.attrs.update({'class': 'input', 'placeholder': placeholder})

class AdminUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'is_staff')

class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', )

class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_field_attributes('username', _('Username'))
        self.set_field_attributes('password', _('Enter Your Password'))

    def set_field_attributes(self, field_name, placeholder):
        self.fields[field_name].widget.attrs.update({'class': 'input', 'placeholder': placeholder})
