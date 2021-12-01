from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact"),
    path('searchprod/', views.searchprod, name="Searchprod"),
    path('checkout/', views.checkout, name="Checkout"),
    path('tracker/', views.tracker, name=" OrderTracker"),
    path("products<int:myid>", views.productView, name="ProductView"),

   # path('contact/', views.contact, name="ContactUs"),
 #   path('tracker/', views.tracker, name="TrackingStatus"),
 #   path('search/', views.search, name="Search"),
  #  path('productView/', views.productView, name="productView"),
   # path('checkout/', views.checkout, name="Checkout"),

]