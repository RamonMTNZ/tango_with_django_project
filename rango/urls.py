from django.urls import path
from rango import views
from registration.backends.simple.views import RegistrationView
from django.urls import reverse

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category,
         name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('goto/', views.goto_url, name='goto'),

]