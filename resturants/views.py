import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

# Create your views here.
#function based views
def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def restaurant_createview(request):
    form = RestaurantLocationCreateForm( request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        '''
        obj = RestaurantLocation.objects.create(
            name = form.cleaned_data.get('name'),
            location = form.cleaned_data.get('location'),
            category = form.cleaned_data.get('category')
        )
        '''
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        print(form.errors)
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = {'form':form, 'errors': errors}

    return render(request, template_name, context)

class RestaurantListView(ListView):
    #queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        #print (self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset =  RestaurantLocation.objects.filter(
                Q(category__iexact=slug) | Q(category__iexact=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurantlocation_detail.html'
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    login_url = '/login/'
    success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        #instance.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        num = random.randint(0, 1000000)
        context = {"html_var": "Context Variable", "rand_num": num}
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
