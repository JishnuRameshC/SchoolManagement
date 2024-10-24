from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import LoginForm



class LoginView(View):
    template_name = 'registration/login.html'
    
    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                if user.role == 'admin' or user.is_superuser:
                    return redirect('dashboard')
                elif user.role == 'librarian':
                    return redirect('library-list')
                elif user.role == 'staff':
                    return redirect('student-list')  
                else:
                    return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
        return render(request, self.template_name, {'form': form})
    


    # def get(self, request):
    #     form = AuthenticationForm()
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request):
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None and user.is_active:
    #             login(request, user)  
    #             if user.role == 'admin' or user.is_superuser:
    #                 return redirect('dashboard')  
    #             elif user.role == 'librarian':
    #                 return redirect('librarian')  
    #             elif user.role == 'staff':
    #                 return redirect('staff') 
    #             else:
    #                 return redirect('home')
    #         else:
    #             messages.error(request, "Invalid username or password")
    #     return render(request, self.template_name, {'form': form})