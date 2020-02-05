from django.urls import path
from .views import PassengerListView, PassengerDetailView, DriverDetailView
from django.urls import path, include


urlpatterns = [
    path('', PassengerListView.as_view(), name='passenger-list-page'), 
    path('<str:slug>/', PassengerDetailView.as_view(), name='passenger-details-page'),
    path('<str:slug>/', DriverDetailView.as_view(), name='driver-details-page'),
]