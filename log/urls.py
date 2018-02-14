from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/',auth_views.login, name='login'),
    path('logout/',auth_views.logout, name='logout'),
    path('signup/',views.signup,name='signup'),
]