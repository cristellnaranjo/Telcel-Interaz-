from django.urls import path

from . import views

urlpatterns = [
    path('',views.flight,name='flight'),
    path('delete/<int:id>',views.flightdelete,name='flightdelete'),
    path('add',views.flight_add,name='flight_add'),
    path('flightadd',views.flightadd,name='flightadd'),
    path('get/<int:id>',views.flightget,name='flightget'),
    path('update/<int:id>',views.flightupdate,name='flightupdate'),
    path('flightupdate/<int:id>',views.flight_update,name='flight_update'),
    
]
