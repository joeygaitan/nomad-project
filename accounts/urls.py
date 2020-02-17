from django.urls import path
from accounts.views import SignUpView, Sayhi


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', SignUpView.as_view(), name='signup-page'),
]