from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



urlpatterns = [
    path('',views.index.as_view(),name='index'),

    path('notes',views.index.as_view(),name='notes'),
    path('<str:hashed_id>',views.ModelDetailView.as_view(),name='details'),
    path('create/', views.CreateNewNote.as_view(), name='create'),
    path('update/<str:hashed_id>',views.update_note.as_view(),name='update'),
    path('delete/<str:hashed_id>',views.ModelDeleteView.as_view(),name='delete'),
    
   
     
] 
