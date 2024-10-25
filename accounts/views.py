from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, UserUpdateForm, ChangePasswordForm
from django.contrib.auth import logout
from .models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse


class LoginView(View):
    template_name = 'account/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.first_name} {user.last_name}! You have successfully logged in.')
                if user.role == 'admin' or user.is_superuser:
                    return redirect('dashboard')
                elif user.role == 'librarian':
                    return redirect('library-list')
                elif user.role == 'staff':
                    return redirect('student-list')  
                else:
                    messages.error(request, 'Invalid username or password. Please try again.')
            else:
                form.add_error('username', 'Username does not exist or incorrect password.')
        return render(request, self.template_name, {'form': form})
    

class UserRegistrationView(View):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful.')
            return HttpResponse('Registration successful')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
        return render(request, self.template_name, {'form': form})
    

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect(reverse('login'))
    
class UserUpdateView(View):
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserUpdateForm(instance=user)
        return render(request, 'account/user_form.html', {'form': form})

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been updated successfully.")
            return redirect(reverse_lazy('dashboard'))
        return render(request, 'account/user_form.html', {'form': form})


class UserDeleteView(View):
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        return render(request, 'account/user_confirm_delete.html', {'user': user})

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        messages.success(request, "User has been deleted successfully.")
        return redirect(reverse_lazy('dashboard'))
    
class ChangePasswordView(View):
    template_name = 'account/change_password.html'
    form_class = ChangePasswordForm

    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = self.form_class(user=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = self.form_class(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Password has been changed successfully.")
            return redirect(reverse_lazy('dashboard'))
        return render(request, self.template_name, {'form': form})