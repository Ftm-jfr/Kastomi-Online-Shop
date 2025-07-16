from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser

        fields = [
            'full_name', 'national_code', 'education', 'job',
            'date_of_birth', 'email', 'password', 'confirm_password'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'style': 'text-align:right; color:#656565;'}),
            'national_code': forms.NumberInput(attrs={'style': 'text-align:left;'}),
            'education': forms.Select(attrs={'style': 'color:#656565;'}),
            'job': forms.Select(attrs={'style': 'color:#656565;'}),
            'date_of_birth': forms.TextInput(),
            'email': forms.EmailInput(attrs={'style': 'text-align:left;'}),
            'password': forms.PasswordInput(attrs={'placeholder': '********'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': '********'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='شماره موبایل',
        widget=forms.TextInput(attrs={
            'placeholder': 'شماره موبایل',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور',
            'class': 'form-control'
        })
    )


class UserInfoForm(forms.Form):
    full_name = forms.CharField()
    national_code = forms.CharField()
    job = forms.ChoiceField(choices=CustomUser.JOB_CHOICES, required=False)
    education = forms.ChoiceField(choices=CustomUser.EDUCATION_CHOICES, required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

from django import forms
from accounts.models import Province, City

class ContactInfoForm(forms.Form):
    mobile_number = forms.CharField()
    telephone_number = forms.CharField()
    province = forms.ModelChoiceField(queryset=Province.objects.all(), empty_label="انتخاب کنید")
    city = forms.ModelChoiceField(queryset=City.objects.none(), empty_label="ابتدا استان را انتخاب کنید")
    postal_code = forms.CharField()
    full_address = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'data' in kwargs:
            province = kwargs['data'].get('province')
        elif len(args) > 0:
            province = args[0].get('province')
        else:
            province = None

        if province:
            self.fields['city'].queryset = City.objects.filter(province_id=province)
        else:
            self.fields['city'].queryset = City.objects.none()


class AccountInfoForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = [
            'full_name',
            'national_code',
            'education',
            'job',
            'date_of_birth',
            'email',
            'password',
            'confirm_password',
        ]
        widgets = {
            'full_name' : forms.TextInput(attrs={'class': 'input-field'}),
            'national_code' : forms.TextInput(attrs={'class': 'input-field  left-place'}),
            'education' : forms.Select(attrs={'class': 'input-field custom-select'}),
            'job' : forms.Select(attrs={'class': 'input-field custom-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'input-field left-place'}),
            'email' : forms.EmailInput(attrs={'class': 'input-field left-place'}),
            'password' : forms.PasswordInput(attrs={'class': 'input-field'}),
            'confirm_password' : forms.PasswordInput(attrs={'class': 'input-field'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'رمز عبور و تکرار آن یکسان نیستند.')

        return cleaned_data