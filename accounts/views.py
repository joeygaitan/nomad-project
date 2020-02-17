from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Passenger, Driver
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'

