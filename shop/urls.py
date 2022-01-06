from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name="shophome"),
    path('',views.index,name="shophome"),
    path('about/',views.about,name="aboutus"),
    path('contact/',views.contact,name="contactus"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="search"),
    path('products/<int:myid>',views.productView,name="search"),
    path('checkout/',views.checkout,name="checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]

