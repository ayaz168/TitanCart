from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup,name="signup"),
    path('login', views.loginH,name="login"),
    path('logoutH', views.logoutH,name="logoutH"),
    path('contact-us',views.contactus,name="contact-us"),
]