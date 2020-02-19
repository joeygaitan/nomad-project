from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreateForm, ProfileForm
from django.contrib import messages
from accounts.models import Profile
from django.views.generic.list import ListView


class SignUpView(CreateView):
    
    
    # def get(self, request):
  form_class = UserCreateForm
  success_url = reverse_lazy('login')
  
  # This works because using the CreatView and using template name with it to show the page
  template_name = 'registration/signup.html'
        # return render(request, template_name, {
        #   'form': form_class
        # })


class Sayhi(CreateView):
  def get(self, request):
      return render(request, "base.html")

class Homepage(CreateView):
    def get(self, request):
        return render(request, "accounts/home.html")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('index-page')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'profile_form': profile_form
    })

class ProfilesListView(ListView):
    """ Renders a list of all Pages. """
    model = Profile

    def get(self, request):
        """ GET a list of Pages. """
        profiles = self.get_queryset().all()
        return render(request, 'accounts/profile_list.html', {
          'profiles': profiles
        })