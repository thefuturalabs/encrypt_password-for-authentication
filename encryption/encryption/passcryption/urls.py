from django.urls import path
from . import views

urlpatterns = [
     path('',views.signup,name='sign'),
     path('login_new',views.de_login,name='login_new'),
     path('welcome',views.index,name='index'),
     path('otpver/<int:OTP>,<str:uname>/', views.otpstat, name='otpstat')

    ]