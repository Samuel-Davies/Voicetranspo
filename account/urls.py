from django.urls import path
from . import views
app_name = "account"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about_us', views.about_us, name='about_us'),
    path('how_it_works', views.how_it_works, name='how_it_works'),
]