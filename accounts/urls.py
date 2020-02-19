from django.urls import path
from accounts.views import SignUpView, Sayhi, update_profile, ProfilesListView, Homepage


from . import views

urlpatterns = [
    path('', Homepage.as_view(), name='home-page'),
    path('sign_up/', SignUpView.as_view(), name='signup-page'),
    path('say_hi/', Sayhi.as_view(), name="sayhi-page"),
    path('update_profile/', update_profile, name='update-profile-page'),
    path('profiles/', ProfilesListView.as_view(), name='list-profile-page')

]