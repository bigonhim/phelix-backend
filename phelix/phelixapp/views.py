from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
# from django.contrib.auth.mixins import LoginRequiredMixinfrom 
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from .forms import WorkerRegistrationForm, EmployerRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'index.html')

def worker_login(request):
    return render(request,'worker_login.html')

def employer_login(request):
    return render(request,'employer_login.html')

def worker_registration(request):
    return render(request,'worker_register.html')

def employer_registration(request):
    return render(request,'employer_register.html')

def employer_dashboard(request):
    return render(request,'employer_dasboard.html')

@login_required
def employer_dashboard(request):
    return render(request,'employer_dashboard.html',{'user': request.user})

@login_required
def worker_dashboard(request):
    return render(request,'worker_dashboard.html',{'user': request.user})


class CustomLoginView(LoginView):
    template_name = 'worker_login.html'
    next_page = 'home' 
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)  # Log in the user
        # print(f"User authenticated: {self.request.user.is_authenticated}") 

        # Redirect based on user type
        if user.user_type == 'worker':
            return redirect('/worker_dashboard')
        elif user.user_type == 'employer':
            return redirect('/employer_dashboard')
        return super().form_valid(form)  # Uses next_page as fallback    

def register_worker(request):
    if request.method == "POST":
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the worker to the database
            return redirect('worker_login')  # Redirect to login page
        else:
            print(form.errors)  # Print form errors in terminal

    else:
        form = WorkerRegistrationForm()

    return render(request, 'worker_register.html', {'form': form})



def register_employer(request):
    if request.method == "POST":
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the worker to the database
            return redirect('employer_login')  # Redirect to login page
        else:
            print(form.errors)  # Print form errors in terminal

    else:
        form = EmployerRegistrationForm()

    return render(request, 'employer_register.html', {'form': form})





