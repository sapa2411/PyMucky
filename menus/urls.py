from django.conf.urls import url
from menus.views import (
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView
)

from django.contrib.auth.views import LoginView


app_name = 'menus'

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
]
