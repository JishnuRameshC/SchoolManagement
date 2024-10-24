from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student,LibraryRecord,FeesRecord
from .forms import StudentForm,LibraryForm,FeesForm

class RoleRequiredMixin(UserPassesTestMixin):
    allowed_roles = []

    def test_func(self):
        return self.request.user.role in self.allowed_roles


# Admin Views
class AdminDashboardView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Student
    template_name = 'dashboard.html'
    role_required = 'staff'
    allowed_roles = ['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_student'] = Student.objects.count()
        context['total_library'] = LibraryRecord.objects.count()
        context['total_fees'] = FeesRecord.objects.count()
        return context
    
    
class StudentCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student-list')
    allowed_roles = ['admin', 'staff']

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/student_list.html'

class StudentUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student-list')
    allowed_roles = ['admin', 'staff']

class StudentDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
    allowed_roles = ['admin', 'staff']

class LibaryCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = LibraryRecord
    form_class = LibraryForm
    template_name = 'librarys/library_form.html'
    success_url = reverse_lazy('library-list')
    allowed_roles = ['admin', 'staff']

    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)
    
class LibraryListView(LoginRequiredMixin, ListView):
    model = LibraryRecord
    template_name = 'librarys/library_list.html'


class LibaryUpdateView(LoginRequiredMixin, RoleRequiredMixin,UpdateView):
    model = LibraryRecord
    form_class = LibraryForm
    template_name = 'librarys/library_form.html'
    success_url = reverse_lazy('library-list')
    allowed_roles = ['admin', 'staff']

class LibraryDeleteView(LoginRequiredMixin, RoleRequiredMixin,DeleteView):
    model = LibraryRecord
    template_name = 'librarys/library_confirm_delete.html'
    success_url = reverse_lazy('library-list')
    allowed_roles = ['admin', 'staff']


class FeesListView(LoginRequiredMixin, RoleRequiredMixin,ListView):
    model = FeesRecord
    template_name = 'fees/fees_list.html'
    allowed_roles = ['admin', 'staff']


class FeesCreateView(LoginRequiredMixin, RoleRequiredMixin,CreateView):
    model = FeesRecord
    form_class = FeesForm
    template_name = 'fees/fees_form.html'
    success_url = reverse_lazy('fees-list')
    allowed_roles = ['admin', 'staff']
    def form_valid(self, form):
        print("Form is valid!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid!", form.errors)
        return super().form_invalid(form)

class FeesUpdateView(LoginRequiredMixin, RoleRequiredMixin,UpdateView):
    model = FeesRecord
    form_class = FeesForm
    template_name = 'fees/fees_form.html'
    success_url = reverse_lazy('fees-list')
    allowed_roles = ['admin', 'staff']

class FeesDeleteView(LoginRequiredMixin, RoleRequiredMixin,DeleteView):
    model = FeesRecord
    template_name = 'fees/fees_confirm_delete.html'
    success_url = reverse_lazy('fees-list')
    allowed_roles = ['admin', 'staff']

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
