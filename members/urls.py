from django.urls import path
from . import views as v

urlpatterns = [
    path('register/', v.UserRegistrationView.as_view(), name="register"),
    
]