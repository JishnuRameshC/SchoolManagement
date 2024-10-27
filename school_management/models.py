from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

from accounts.models import CustomUser
from django.conf import settings

# Create your models here.
class GradeSection(models.Model):
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    class Meta:
        unique_together = ('grade', 'section')

    def __str__(self):
        return f"{self.grade} - {self.section}"

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=True)
    registration_number = models.CharField(max_length=20, unique=True,null=True)
    student_number = models.AutoField(primary_key=True)
    dob = models.DateField(verbose_name='Date of Birth')
    grade_section = models.ForeignKey(GradeSection,null=True, on_delete=models.SET_NULL)
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
        return f"{self.registration_number} ,  {self.first_name} {self.last_name} , class : {self.grade_section}"
    
    class Meta:
        ordering = ['grade_section', 'first_name', 'last_name']



class FeesRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    payment_status_choices =(
            ('pending', 'Pending'),
            ('partial', 'Partially Paid'),
            ('paid', 'Paid'),
        )
    payment_status = models.CharField(
        max_length=20,
        choices=payment_status_choices,
        default='pending',)
    remarks = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.registration_number} - {self.fee_type} - {self.amount}"

    class Meta:
        ordering = ['-created_at']
