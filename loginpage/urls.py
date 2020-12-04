from django.urls import path

from . import views

urlpatterns = [
    
    #path('createaccount/', createaccountPageView, name='createaccount'),
    path('register/', views.registerPage, name='register'),

    #path('login/', views.loginPage, name="login"),
    #path('logout/', views.logoutUser, name="logout"),

    path('', views.indexPageView, name='index'),
]