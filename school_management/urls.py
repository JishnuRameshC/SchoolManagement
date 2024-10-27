from django.urls import path
from .views import StudentListView, StudentCreateView,StudentUpdateView,StudentDeleteView
from .views import FeesListView, FeesCreateView,FeesUpdateView,FeesDeleteView,DashboardView,GradeSectionView
from .views import GradeSectionUpdateView,GradeSectionDeleteView

urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('grade-section/', GradeSectionView.as_view(), name='grade-section'),
    path('grade-section/update/<int:pk>/', GradeSectionUpdateView.as_view(), name='grade-section-update'),
    path('grade-section/delete/<int:pk>/', GradeSectionDeleteView.as_view(), name='grade-section-delete'),

    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/create/', StudentCreateView.as_view(), name='student-create'),
    path('student/update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    

    path('fees/', FeesListView.as_view(), name='fees-list'),
    path('fees/create/', FeesCreateView.as_view(), name='fees-create'),
    path('fees/update/<int:pk>/', FeesUpdateView.as_view(), name='fees-update'),
    path('fees/delete/<int:pk>/', FeesDeleteView.as_view(), name='fees-delete'),

    # path('librarian/<int:pk>/', LibrarianStudentDetailView.as_view(), name='librarian-student-detail'),
    # path('staff/', StaffStudentListView.as_view(), name='staff-student-list'),
]
