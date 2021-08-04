from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [

    url(r'^$', Index.as_view(), name='index'),
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^logout/$', admin_logout, name='logout'),
    url(r'^team/(?P<pk>\d+)$', TeamDetails.as_view(), name='team-details'),
    url(r'^team-registration/$', AddTeam.as_view(), name='add-team'),
    url(r'^registration-success/$', TeamRegistrationSuccess.as_view(), name='registration-success'),
    path('add/', addPhoto, name='add'),
    path('update-photo/<str:pk>/', UpdatePhoto, name='update_photo'),
    path('delete-photo/<str:pk>/', DeletePhoto, name='delete_photo'),
    path('delete-category/<str:pk>/', DeleteCategory, name='delete_category'),
    path('delete-point/<str:pk>/', DeletePoint, name='delete_point'),

]
