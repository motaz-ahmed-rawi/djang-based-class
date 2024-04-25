from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/',views.signUp,name= 'signup'),
    
    path('home/',views.home,name= 'home'),
    path('logout/',auth_views.LogoutView.as_view(),name= 'logout'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts\login.html'),name='login'),
]

 