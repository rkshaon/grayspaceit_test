from django.urls import path
from authentication.views import loginPage, register

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', register, name='register'),
]
