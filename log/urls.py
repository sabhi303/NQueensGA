from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="login page"),
    path('logout',views.logout,name="SignUP page"),
    path('signup',views.signup,name="SignUP page"),

]
	