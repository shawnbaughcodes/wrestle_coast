from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'company_home'),
    url(r'^logout$', views.logout, name = 'company_logout'),

]
