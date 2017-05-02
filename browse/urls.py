from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'browse_home'),
    url(r'^logout$', views.logout, name = 'browse_logout'),

]
