from django.contrib import admin
from accounts.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_profile = ('bio', 'location', 'birth_date')

admin.site.register(Profile, ProfileAdmin)
