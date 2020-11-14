from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('/tutoring/', views.tutoring, name='tutoring'),
    path('/about/', views.about, name='about'),
    path('/sponsor/', views.sponsor, name='sponsor'),
    path('/login/', views.login, name='login'),
    path('/contact/', views.contact, name='contact'),
    path('/apply/', views.apply, name='apply')
 
    

]