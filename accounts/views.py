from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Passenger, Driver


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PassengerListView(ListView):
    """ Renders a list of all People. """
    model = Passenger

    def get(self, request):
        """ GET a list of passengers. """
        people = self.get_queryset().all()
        return render(request, 'list.html', {
          'people': people
        })

class PassengerDetailView(DetailView):
    """ Renders a specific passenger based on it's slug."""
    model = Passenger

    def get(self, request, slug):
        """ Returns a specific passenger page by slug. """
        passenger = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'passenger.html', {
          'passenger': passenger
        })

class DriverDetailView(DetailView):
    """ Renders a specific driver based on it's slug."""
    model = Driver

    def get(self, request, slug):
        """ Returns a specific driver page by slug. """
        driver = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'driver.html', {
          'driver': driver
        })