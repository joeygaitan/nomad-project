from django.urls import path
from accounts.views import SignUpView, Sayhi, update_profile


from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('sign_up/', SignUpView.as_view(), name='signup-page'),
    path('say_hi/', Sayhi.as_view(), name="home-page"),
    path('update_profile/', update_profile, name='update-profile-page')
]