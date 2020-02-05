from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Passenger(models.Model):
    """ Represents a single passenger. """
    location = models.CharField(max_length=100, 
                             help_text="Where you are located.")
    author = models.ForeignKey(User, on_delete=models.PROTECT, unique=True,
                               help_text="Name of passenger.")
    slug = models.CharField(max_length=100, blank=True, editable=False,
                            help_text="Unique URL path to access this person. Generated by the system.")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this request was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this request was updated. Automatically generated when the model updates.")
    
    def __str__(self):
        return self.author

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/passenger). """
        path_components = {'slug': self.slug}
        return reverse('passenger-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new passenger is created. """
        if not self.pk:
            self.slug = slugify(self.author, allow_unicode=True)

        # Call save on the superclass.
        return super(Page, self).save(*args, **kwargs)


class Driver(models.Model):
    """ Represents a single driver. """
    car = models.CharField(max_length=50, 
                             help_text="What you are driving.")
    author = models.ForeignKey(User, on_delete=models.PROTECT, unique=True,
                               help_text="Name of driver.")
    slug = models.CharField(max_length=100, blank=True, editable=False,
                            help_text="Unique URL path to access this person. Generated by the system.")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time availability was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time availability was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/driver). """
        path_components = {'slug': self.slug}
        return reverse('driver-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new driver is created. """
        if not self.pk:
            self.slug = slugify(self.author, allow_unicode=True)

        # Call save on the superclass.
        return super(Page, self).save(*args, **kwargs)