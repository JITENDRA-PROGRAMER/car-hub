from django.urls import path

from pages import views

from .import views
urlpatterns = [
   path('',views.Cars,name="cars"),
   path('<int:id>',views.Car_detail,name="car_detail"),
   path('search',views.Search,name="search"),
]
