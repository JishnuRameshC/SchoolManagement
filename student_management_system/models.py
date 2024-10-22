from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=True)
    student_number = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField(verbose_name='Date of Birth')
    address = models.TextField()
    grade = models.CharField(max_length=10, verbose_name="Class/Grade")

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.student_number}) {self.full_name} ({self.email})"

class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    borrowed_at = models.DateTimeField(auto_now_add=True)

class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)