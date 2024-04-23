from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('',views.PostList.as_view(),name='post_list'),
path('<int:pk>',views.PostDetail.as_view()),
path('create',views.PostCreate.as_view(), name='post_create'),
path('delete/<int:pk>',views.PostDelete.as_view(), name='post_delete'),
path('update/<int:pk>',views.PostUpdate.as_view(), name='post_update'),
]

