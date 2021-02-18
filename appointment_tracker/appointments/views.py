from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404
from .forms import RegisterForm
from django.template import loader
from .models import Application, Reply


# Create your views here.
def user_register(request):
    template = 'appointments/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Password do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                login(request, user)

                return HttpResponseRedirect('appointments/account')
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


# def home_page(request):
#     latest_application_list = Application.objects.order_by('pub_date')[:5]
#     context = {
#         'latest_application_list': latest_application_list
#     }
#     # return HttpResponse("Hello, world. You're at the appointments home page.")
#     return render(request, 'appointments/home_page.html', context)
class Home_PageView(generic.ListView):
    template_name = 'appointments/home_page.html'
    context_object_name = 'latest_application_list'

    def get_queryset(self):
        return Application.objects.order_by('pub_date')[:5]


# def detail(request, application_id):
#     application = get_object_or_404(Application, pk=application_id)
#     # return HttpResponse("You're looking at application %s." % application_id)
#     return render(request, 'appointments/login.html', {'application': application})
class DetailView(generic.DetailView):
    model = Application
    template_name = 'appointments/login.html'


# def results(request, application_id):
#     # response = "You're looking at the results of application %s."
#     # return HttpResponse(response % application_id)
#     application = get_object_or_404(Application, pk=application_id)
#     return render(request, 'appointments/results.html', {'application': application})
class ResultsView(generic.DetailView):
    model = Application
    template_name = 'appointments/results.html'


def vote(request, application_id):
    # return HttpResponse("You're voting for application %s." % application_id)
    application = get_object_or_404(Application, pk=application_id)
    try:
        selected_reply = application.reply_set.get(pk=request.POST['reply'])
    except (KeyError, Reply.DoesNotExist):
        return render(request, 'appointments/login.html', {
            'application': application,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_reply.votes += 1
        selected_reply.save()
        return HttpResponseRedirect(reverse('appointments:results', args=(application.id,)))
