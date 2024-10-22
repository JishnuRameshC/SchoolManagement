from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from accounts.models import CustomUser
from django.conf import settings

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    registration_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=True)
    student_number = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField(verbose_name='Date of Birth')
    address = models.TextField()
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=5)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.registration_number} - {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['grade', 'section', 'first_name']

class LibraryRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_records')
    book_title = models.CharField(max_length=200)
    book_id = models.CharField(max_length=50)
    borrowed_date = models.DateField()
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.registration_number} - {self.book_title}"

class FeesRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    fee_type = models.CharField(max_length=50)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('partial', 'Partially Paid'),
            ('paid', 'Paid'),
        ],
        default='pending'
    )
    remarks = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.registration_number} - {self.fee_type} - {self.amount}"
