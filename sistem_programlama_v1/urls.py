from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.faculty_list, name='faculty_list'),
]