from django.urls import path
from .views import LibraryListView, LibraryCreateView,LibraryUpdateView,LibraryDeleteView
from .views import LibraryRecordListView, LibraryRecordCreateView,LibraryRecordUpdateView,LibraryRecordDeleteView
urlpatterns = [
    path('library/', LibraryListView.as_view(), name='library-list'),
    path('library/create/', LibraryCreateView.as_view(), name='library-create'), 
    path('library/update/<int:pk>/', LibraryUpdateView.as_view(), name='library-update'), 
    path('library/delete/<int:pk>/', LibraryDeleteView.as_view(), name='library-delete'),
    
    path('libraryrecord/', LibraryRecordListView.as_view(), name='libraryrecord-list'),
    path('libraryrecord/create/', LibraryRecordCreateView.as_view(), name='libraryrecord-create'), 
    path('libraryrecord/update/<int:pk>/', LibraryRecordUpdateView.as_view(), name='libraryrecord-update'), 
    path('libraryrecord/delete/<int:pk>/', LibraryRecordDeleteView.as_view(), name='libraryrecord-delete'),
]

   