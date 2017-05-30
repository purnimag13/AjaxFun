from django.conf.urls import url
from django.contrib import admin
from places.views import CountryListView, StateListView

urlpatterns = [
    url(r'^countries/$', CountryListView.as_view(), name='country_list_view'),
    url(r'^states/$', StateListView.as_view(), name='state_list_view'),
]
