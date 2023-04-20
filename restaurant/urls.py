from django.contrib import admin
from django.urls import path, include
from . import views

#For APIView Viewset based views
from rest_framework.routers import DefaultRouter
#Create router
router = DefaultRouter()
#Register views based on viewsets with router
router.register(r'menuv',views.MenuViewset,basename='menuv')
router.register(r'bookingv',views.BookingViewset,basename='bookingv')
#Register views based on Modelviewsets with router
router.register(r'menum',views.MenuModelViewset,basename='menum')
router.register(r'bookingm',views.BookingModelViewset,basename='bookingm')

urlpatterns = [    
    path('menu',views.MenuView.as_view()),
    path('booking',views.BookingView.as_view()),
    #paths for viewsets registered with router    
    path('',include(router.urls)),
    #paths for Generic views
    path('menug',views.MenuGenericView.as_view()),
    path('bookingg',views.BookingGenericView.as_view()),
]
