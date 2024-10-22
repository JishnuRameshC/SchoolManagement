from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)  
                if user.role == 'admin' or user.is_superuser:
                    return redirect('dashboard')  
                elif user.role == 'librarian':
                    return redirect('librarian')  
                elif user.role == 'staff':
                    return redirect('staff') 
                else:
                    return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        return render(request, self.template_name, {'form': form})