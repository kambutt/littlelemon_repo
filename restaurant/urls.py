from django.contrib import admin
from django.urls import path, include
from . import views

#Router based stuff is done at project level
#For class based, APIViews and Generic views urls are defined here

urlpatterns = [    
    #path('menu',views.MenuView.as_view()),
    #path('booking',views.BookingView.as_view()),
    #paths for Generic views
    #path('menug',views.MenuGenericView.as_view()),
    #path('bookingg',views.BookingGenericView.as_view()),
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
]
