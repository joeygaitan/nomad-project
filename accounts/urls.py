from django.urls import path
from accounts.views import SignUpView, Sayhi, update_profile, ProfilesListView, Homepage, GetRiders, login_view_profile, ConfirmPage


from . import views

urlpatterns = [
    path('', Homepage.as_view(), name='home-page'),
    path('sign_up/', SignUpView.as_view(), name='signup-page'),
    path('say_hi/', Sayhi.as_view(), name="sayhi-page"),
    path('get_ride/', update_profile, name='get-ride-page'),
    path('get_riders/', GetRiders.as_view(), name='get-riders-page'),
    path('all_rides/', ProfilesListView.as_view(), name='list-rides-page'),
    path('profile/', login_view_profile, name='account-page'), 
    path('confirm/', ConfirmPage.as_view(), name='confirm-page')
]