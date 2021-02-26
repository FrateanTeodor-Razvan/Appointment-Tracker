from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from .models import Appointment


@login_required
def home_page_view(request):
    search = request.GET.get('search')
    if search:
        appointment = Appointment.objects.filter(appointment_text__icontains=search)
    else:
        appointment = Appointment.objects.all()
    context = {
        'appointment': appointment
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
            print("Is valid")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("home_page")
    return render(request=request, template_name="appointments/login.html", context={"login_form": form})
#     # return render(request=request, template_name="appointments/login.html")


# def login_view(request):
#     return render(request, "appointments/login.html")


# @login_required
# def home(request):
#     return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect("home_page")


class AppointmentTemplate(TemplateView):
    template_name = "appointments/appointment_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = 'template_view is working'
        return context


class AppointmentList(ListView):
    template_name = "appointments/appointment_list.html"
    model = Appointment
    context_object_name = 'appointment_list'
    # success_url = reverse_lazy('appointments:appointment_list')

    def get_queryset(self):
        qs = super(AppointmentList, self).get_queryset()
        return qs.order_by('appointment_id')

    def get_context_data(self, **kwargs):
        context = super(AppointmentList, self).get_context_data(**kwargs)
        context['status'] = 'list_view is working'
        return context


class AppointmentCreate(CreateView):
    template_name = "appointments/appointment_create.html"
    model = Appointment
    fields = '__all__'
    success_url = reverse_lazy('appointments:appointment_list')

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user_id = self.request._id
    #     self.object.save()
    #     return super().form_valid(form)


class AppointmentDetail(DetailView):
    template_name = "appointments/appointment_detail.html"
    model = Appointment
    pk_url_kwarg = 'appointment_id'
    context_object_name = 'appointment_detail'

    def get_context_data(self, **kwargs):
        context = super(AppointmentDetail, self).get_context_data(**kwargs)
        context['status'] = 'detail_view is working'
        return context


class AppointmentUpdate(UpdateView):
    template_name = "appointments/appointment_update.html"
    model = Appointment
    fields = ('department_id', 'appointment_text')
    success_url = reverse_lazy('appointments:appointment_list')
    pk_url_kwarg = 'appointment_id'


class AppointmentDelete(DeleteView):
    template_name = "appointments/appointment_delete.html"
    model = Appointment
    context_object_name = 'appointment'
    success_url = reverse_lazy('appointments:appointment_list')
