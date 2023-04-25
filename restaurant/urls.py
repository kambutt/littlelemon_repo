from django.contrib import admin
from django.urls import path, include
from . import views

#Router based stuff is done at project level
#For class based, APIViews and Generic views urls are defined here

urlpatterns = [    
    path('menu/',views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
    path('message',views.msg),
]
