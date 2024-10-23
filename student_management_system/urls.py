from django.urls import path
from .views import StudentListView, StudentCreateView,StudentUpdateView,StudentDeleteView, LibraryListView, LibaryCreateView,LibaryUpdateView,LibraryDeleteView
from .views import FeesListView, FeesCreateView,FeesUpdateView,FeesDeleteView
urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    
    path('library/', LibraryListView.as_view(), name='library-list'),
    path('library/create/', LibaryCreateView.as_view(), name='library-create'),
    path('library/update/<int:pk>/', LibaryUpdateView.as_view(), name='library-update'),
    path('library/delete/<int:pk>/', LibraryDeleteView.as_view(), name='library-delete'),

    path('fees/', FeesListView.as_view(), name='fees-list'),
    path('fees/create/', FeesCreateView.as_view(), name='fees-create'),
    path('fees/update/<int:pk>/', FeesUpdateView.as_view(), name='fees-update'),
    path('fees/delete/<int:pk>/', FeesDeleteView.as_view(), name='fees-delete'),

    # path('librarian/<int:pk>/', LibrarianStudentDetailView.as_view(), name='librarian-student-detail'),
    # path('staff/', StaffStudentListView.as_view(), name='staff-student-list'),
]
