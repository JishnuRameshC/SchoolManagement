from datetime import date
from django import forms
from .models import Student,LibraryRecord,FeesRecord
from django.core.validators import EmailValidator
from django.forms import CharField, TextInput, DateField, ChoiceField, DateInput
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    first_name = CharField(
        label="First Name",
        max_length=30,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    last_name = CharField(
        label="Last Name",
        max_length=30,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    email = CharField(
        min_length=5,
        max_length=50,
        label="Email",
        required=True,
        validators=[EmailValidator()],
        widget=TextInput(attrs={"class": "form-control"}),
    )
    phone_number = CharField(
        label="Phone Number",
        max_length=15,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    dob = DateField(
        label="Date of Birth",
        required=True,
        widget=DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    address = CharField(
        label="Address",
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    grade = ChoiceField(
        label="Grade",
        choices=[('10th', '10th'), ('11th', '11th'), ('12th', '12th'), ('graduated', 'Graduated'), ('other', 'Other')],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    gender = ChoiceField(
        label="Gender",
        choices=[
            ('M', 'Male'),
            ('F', 'Female')
        ],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )


    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'dob', 'address', 'grade', 'gender']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Get the current instance (if any) being updated
            current_instance = getattr(self, 'instance', None)
            if current_instance and Student.objects.filter(email=email).exclude(pk=current_instance.pk).exists():
                raise ValidationError("A user with this email already exists.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            # Get the current instance (if any) being updated
            current_instance = getattr(self, 'instance', None)
            if current_instance and Student.objects.filter(phone_number=phone_number).exclude(pk=current_instance.pk).exists():
                raise ValidationError("A user with this phone number already exists.")
        return phone_number

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')

        if dob and dob >= date.today():
            raise ValidationError("Date of Birth must be in the past.")
        return dob

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        # Check if both first name and last name are provided
        if not first_name or not last_name:
            raise ValidationError("Both first name and last name are required.")
        

class LibraryForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = ['student', 'book_title', 'book_id', 'borrowed_date', 'due_date', 'remarks']

    student = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    book_title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_id = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    borrowed_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    remarks = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class FeesForm(forms.ModelForm):
    class Meta:
        model = FeesRecord
        fields = '__all__'

    due_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    paid_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    payment_status = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}))
    remarks = ChoiceField(
        label="Remarks",    
        choices=[],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
