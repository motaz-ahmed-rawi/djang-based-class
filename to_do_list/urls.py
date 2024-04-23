from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.signup.as_view(),name='index'),
    path('notes',views.index.as_view(),name='notes'),
    path('<int:pk>',views.ModelDetailView.as_view(),name='details'),
    path('update/<int:pk>',views.update_note.as_view(),name='update'),
    path('login',views.login,name='login'),
    
]
