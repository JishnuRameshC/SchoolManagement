from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    LibrarianStudentDetailView, StaffStudentListView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('librarian/<int:pk>/', LibrarianStudentDetailView.as_view(), name='librarian-student-detail'),
    path('staff/', StaffStudentListView.as_view(), name='staff-student-list'),
]
