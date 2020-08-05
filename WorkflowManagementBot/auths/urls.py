from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
urlpatterns =[

    path('signin/',  views.signin_request, name='signin'),
    path('signout', LogoutView.as_view(template_name='auths/logout.html'), name='signout'),
    path('signup/', views.signup_request, name='signup'),


]