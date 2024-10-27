from django.db import models
from school_management.models import Student
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Library(models.Model):
    book_title = models.CharField(max_length=200)
    book_id = models.CharField(max_length=20, unique=True)
    quantity = models.IntegerField()
    curent_quantity = models.IntegerField(default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_title} - ({self.book_id}) - Total quantity {self.quantity} -remaining : {self.curent_quantity}"

    class Meta:
        ordering = ['-created_at']


class LibraryRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='library_records')
    borrowed_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='borrowed')
    returned_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.full_name} (Grade {self.student.grade}, Section {self.student.section}) - {self.book_title}"

    class Meta:
        ordering = ['-created_at']