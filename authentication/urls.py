from django.urls import path
from authentication.views import loginPage, logoutPage, register

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', register, name='register'),
]
