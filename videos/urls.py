from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('thanks/', views.thanks, name='thanks'),
    path('create/', views.create_video, name='create_video'),
    path('speaker-list/', views.speakersList, name='speakersList'),
    path('choose-register/', views.choose_register, name='choose_register'),
    path('create-student/',views.StudentSignUpView.as_view(), name='student_signup'),
    path('create-speaker/',views.SpeakerSignUpView.as_view(), name='speaker_signup'),
    path('<int:video_id>/', views.detail, name='detail'),
]