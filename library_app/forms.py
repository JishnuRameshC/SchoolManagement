from django import forms
from .models import Library, LibraryRecord
from django.core.exceptions import ValidationError
from datetime import date
from django.forms import ModelForm, ModelChoiceField
from school_management.models import Student


class LibraryForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    book_title = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    book_id = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Library
        fields = ["book_title", "book_id", "quantity"]



    def clean_book_id(self):
        book_id = self.cleaned_data.get("book_id")
        instance = getattr(self, "instance", None)
        if (
            Library.objects.filter(book_id=book_id)
            .exclude(pk=instance.pk if instance else None)
            .exists()
        ):
            raise ValidationError("This Book ID already exists.")
        return book_id


class LibraryRecordForm(forms.ModelForm):

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )

    remarks = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
    )

    book = ModelChoiceField(
        label="Book",
        queryset=Library.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    student = ModelChoiceField(
        label="Student",
        queryset=Student.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    status_choice = (
        ("Borrowed", "Borrowed"),
        ("Returned", "Returned"),
        ("Overdue", "Overdue"),
    )

    status = forms.ChoiceField(
        label="Status",
        choices=status_choice,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = LibraryRecord
        fields = ["student", "book", "due_date", "remarks", "status"]

    def clean_returned_date(self):
        returned_date = self.cleaned_data.get("returned_date")
        if returned_date and returned_date < date.today():
            raise ValidationError("Returned date cannot be in the past.")
        return returned_date

    def clean_due_date(self):
        due_date = self.cleaned_data.get("due_date")
        if due_date and due_date < date.today():
            raise ValidationError("Due date cannot be in the past.")
        return due_date
    
    def clean_book(self):
        book = self.cleaned_data.get("book")
        if book.quantity == 0:
            raise ValidationError("Book is out of stock.")
        return book

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        