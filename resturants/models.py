from django.conf import  settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.

User = settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name #obj.title

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving..')
    print(instance.created_at)
    if not instance.slug:
        print('inside')
        instance.slug = unique_slug_generator(instance)

def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('saved')
    print(instance.created_at)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)
