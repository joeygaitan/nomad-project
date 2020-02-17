from django.contrib import admin
from accounts.models import Driver, Passenger


class PassengerAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('location', 'slug', 'author', 'created', 'modified')

class DriverAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('car', 'slug', 'author', 'created', 'modified')

admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Driver, DriverAdmin)