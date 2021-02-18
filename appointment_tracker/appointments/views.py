from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


# Create your views here.
def home_page_view(request):
    context = {
        'appointment_entries': [
            {
                'title': 'A title',
                'body': 'And a description.'
            },
            {
                'title': 'A title',
                'body': 'And a description.'
            }
        ]
    }
    return render(request, "appointments/home_page.html", context)


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            password_repeat = form.cleaned_data.get("password_repeat")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            phone_number = form.cleaned_data.get("phone_number")
            user = User.objects.create_user(username, email, password)
            return redirect("login")
    return render(request=request, template_name="appointments/register.html", context={"register_form": form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("home_page")
    return render(request=request, template_name="appointments/login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    return redirect("home_page")
