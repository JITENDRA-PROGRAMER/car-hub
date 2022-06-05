# from tkinter import N
from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home,name="home"),   
    path('about',views.About,name="about"),
    path('servec',views.Servecs,name="servec"),
    path('contact',views.Contact,name="contact"),
]
