"""
URL configuration for Tech_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from Tech_Quiz import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register_view,name='register'),
    path('Tech_Quiz/register/', views.register_view, name='register'),
    path('Tech_Quiz/login/', views.login_view, name='login'),
    path('Tech_Quiz/logout/', views.logout_view, name='logout'),
    path('Tech_Quiz/quiz_home/', views.quiz_home, name='quiz_home'),
    path('Tech_Quiz/result/<int:total_score>/', views.result, name='result'),
    path('Tech_Quiz/submit-quiz/', views.submit_quiz, name='submit_quiz'),
]