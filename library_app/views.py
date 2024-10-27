from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import Library, LibraryRecord
from .forms import LibraryForm, LibraryRecordForm
from datetime import date

class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'librarys/library_list.html'
    context_object_name = 'books'
    paginate_by = 10

class LibraryCreateView(LoginRequiredMixin, CreateView):
    model = Library
    form_class = LibraryForm
    template_name = 'librarys/library_form.html'
    success_url = reverse_lazy('library-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        print(form.instance.created_by)
        print(form.instance.quantity)
        print(form.instance.curent_quantity)
        form.instance.curent_quantity = form.instance.quantity
        messages.success(self.request, 'Book added successfully.')
        return super().form_valid(form)

class LibraryUpdateView(LoginRequiredMixin, UpdateView):
    model = Library
    form_class = LibraryForm
    template_name = 'librarys/library_form.html'
    success_url = reverse_lazy('library-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully.')
        return super().form_valid(form)

class LibraryDeleteView(LoginRequiredMixin, DeleteView):
    model = Library
    template_name = 'librarys/library_confirm_delete.html'
    success_url = reverse_lazy('library-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Book deleted successfully.')
        return super().delete(request, *args, **kwargs)

class LibraryRecordListView(LoginRequiredMixin, ListView):
    model = LibraryRecord
    template_name = 'librarys/library_record_list.html'
    context_object_name = 'records'
    paginate_by = 10

class LibraryRecordCreateView(LoginRequiredMixin, CreateView):
    model = LibraryRecord
    form_class = LibraryRecordForm
    template_name = 'librarys/library_record_form.html'
    success_url = reverse_lazy('libraryrecord-list')


    def form_invalid(self, form):
        print(form.errors)  # Print any form validation errors to the console
        return super().form_invalid(form)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        
        book = form.cleaned_data['book']
        print(book.quantity)
        print(book.curent_quantity)

        # Decrease book quantity
        if book.curent_quantity > 0:
            book.curent_quantity -= 1
            book.save()
            messages.success(self.request, 'Book borrowed successfully.')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'This book is out of stock.')
            return redirect('library-record-list')




class LibraryRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = LibraryRecord
    form_class = LibraryRecordForm
    template_name = 'librarys/library_record_form.html'
    success_url = reverse_lazy('libraryrecord-list')

    def form_valid(self, form):
        if form.instance.status == 'Returned':
            book = form.cleaned_data['book']
            book.quantity += 1
            book.returned_date = date.today()
            print(book.returned_date)

            book.save()


        messages.success(self.request, 'Record updated successfully.')
        return super().form_valid(form)
    

class LibraryRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = LibraryRecord
    template_name = 'librarys/library_record_confirm_delete.html'
    success_url = reverse_lazy('libraryrecord-list')

    def delete(self, request, *args, **kwargs):
        record = self.get_object()
        if not record.returned_date:
            book = record.book
            book.quantity += 1
            book.save()
        messages.success(request, 'Record deleted successfully.')
        return super().delete(request, *args, **kwargs)