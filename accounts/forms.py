from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from django.forms import CharField, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import PasswordChangeForm



class LoginForm(forms.Form):
    username = CharField(
        required=True,
        widget=TextInput({"class": "form-control", "placeholder": "Username"}),
    )

    password = CharField(
        max_length=15,
        min_length=6,
        required=True,
        widget=PasswordInput({"class": "form-control", "placeholder": "Password"}),
    )


class UserRegistrationForm(forms.ModelForm):
    confirm_password = CharField(
        max_length=25,
        min_length=8,
        required=True,
        label="Confirm Password",
        widget=PasswordInput({"class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "password", "confirm_password", "role"]
        
        widgets = {
            "username": TextInput({"class": "form-control"}),
            "email": EmailInput({"class": "form-control"}),
            "password": PasswordInput({"class": "form-control"}),
            "first_name": TextInput({"class": "form-control"}),
            "last_name": TextInput({"class": "form-control"}),
        }
    
    # Define the 'role' field separately
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password
    
    def save(self, commit=True):
        
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'role']  # Include the fields you want to allow editing
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"})  # Adjust based on your role field
        }

    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:  
            user.save()
        return user
    
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    new_password = forms.CharField(
        label="New Password",
        required=True,
        min_length=6,
        max_length=25,
        help_text="Password must be at least 8 characters long",
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    confirm_new_password = forms.CharField(
        label="Confirm New Password",
        required=True,
        min_length=6,
        max_length=25,

        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = CustomUser
    
    
    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Incorrect old password")
        return old_password
    
    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if new_password == self.cleaned_data.get("old_password"):
            raise forms.ValidationError("New password cannot be the same as old password")
        return new_password

    def clean_confirm_new_password(self):
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if confirm_new_password != self.cleaned_data.get("new_password"):
            raise forms.ValidationError("Passwords do not match")
        return confirm_new_password



    
    