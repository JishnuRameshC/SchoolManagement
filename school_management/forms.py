from datetime import date
from django import forms
from .models import Student,LibraryRecord,FeesRecord,GradeSection
from django.core.validators import EmailValidator
from django.forms import CharField, TextInput, DateField, ChoiceField, DateInput,ModelChoiceField
from django.core.exceptions import ValidationError

class GradeSectionForm(forms.ModelForm):
    grade = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Grade'}),
        required=True,
        label="Grade",
        help_text="eg: 1st, 2nd, 3rd, 4th, 5th .."
    )
    section = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Section'}),
        required=True,
        label="Section",
        help_text="eg: A, B, C, D, E .."
    )
    class Meta:
        model = GradeSection
        fields = ['grade', 'section']


class StudentForm(forms.ModelForm):
    first_name = CharField(
        label="First Name",
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    last_name = CharField(
        label="Last Name",
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    registration_number = CharField(
        label="Registration Number",
        max_length=20,
        required=False,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    dob = DateField(
        label="Date of Birth",
        required=True,
        widget=DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    grade_section = ModelChoiceField(
        label="Grade & Section",
        queryset=GradeSection.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    gender = ChoiceField(
        label="Gender",
        choices=Student.GENDER_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        required=True
    )
    parent_name = CharField(
        label="Parent Name",
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    parent_phone = CharField(
        label="Parent Phone",
        max_length=15,
        required=True,
        widget=TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'registration_number',
            'dob',
            'grade_section',
            'gender',
            'address',
            'parent_name',
            'parent_phone'
        ]

    def clean_registration_number(self):
        registration_number = self.cleaned_data.get('registration_number')
        if registration_number:
            current_instance = getattr(self, 'instance', None)
            if current_instance and Student.objects.filter(
                registration_number=registration_number
            ).exclude(pk=current_instance.student_number).exists():
                raise ValidationError("This registration number already exists.")
        return registration_number

    def clean_parent_phone(self):
        phone = self.cleaned_data.get('parent_phone')
        if not phone.isdigit():
            raise ValidationError("Phone number should contain only digits.")
        if len(phone) < 10:
            raise ValidationError("Phone number should be at least 10 digits.")
        return phone

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob and dob >= date.today():
            raise ValidationError("Date of Birth must be in the past.")
        return dob       

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
