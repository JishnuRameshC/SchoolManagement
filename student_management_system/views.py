from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student
from .forms import StudentForm

class RoleRequiredMixin(UserPassesTestMixin):
    role_required = None
    def test_func(self):
        return self.request.user.role == self.role_required

# Admin Views
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'


# class StudentListView(RoleRequiredMixin, ListView):
#     model = Student
#     template_name = 'school/student_list.html'
#     role_required = 'admin'

# class StudentCreateView(RoleRequiredMixin, CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'school/student_form.html'
#     success_url = reverse_lazy('student-list')
#     role_required = 'admin'

# class StudentUpdateView(RoleRequiredMixin, UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'school/student_form.html'
#     success_url = reverse_lazy('student-list')
#     role_required = 'admin'

# class StudentDeleteView(RoleRequiredMixin, DeleteView):
#     model = Student
#     template_name = 'school/student_confirm_delete.html'
#     success_url = reverse_lazy('student-list')
#     role_required = 'admin'

# # Librarian Views
# class LibrarianStudentDetailView(RoleRequiredMixin, DetailView):
#     model = Student
#     template_name = 'school/student_detail.html'
#     role_required = 'librarian'

# # Office Staff Views
# class StaffStudentListView(RoleRequiredMixin, ListView):
#     model = Student
#     template_name = 'school/student_list.html'
#     role_required = 'staff'
