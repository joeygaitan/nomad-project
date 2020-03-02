from django.urls import path

from api.views import ProfileList

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='polls_list'),
]