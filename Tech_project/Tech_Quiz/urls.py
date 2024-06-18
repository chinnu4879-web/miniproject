from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'Tech_Quiz'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('quiz_home/', views.quiz_home, name='quiz_home'),
    path('result/<int:total_score>/', views.result, name='result'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),  
]