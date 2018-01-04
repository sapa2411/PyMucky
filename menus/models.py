from django.conf import settings
from django.db import models
from django.urls import reverse
from resturants.models import RestaurantLocation
# Create your models here.

class Item(models.Model):
    #associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='cascade')
    restaurant = models.ForeignKey(RestaurantLocation, on_delete='cascade')
    #item stuff
    name = models.CharField(max_length=191)
    contents = models.TextField(help_text='Seperate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='Seperate each item by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

    class Meta:
        #reverse updated, then followed by reverse timestamp
        ordering = ['-updated', '-timestamp']
