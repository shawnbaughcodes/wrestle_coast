from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^logging_in$', views.logging_in, name = 'logging_in'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^registration$', views.registration, name = 'registration'),
]
