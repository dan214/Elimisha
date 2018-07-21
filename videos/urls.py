from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_video, name='create_video'),
    path('<int:video_id>/', views.detail, name='detail'),
]