"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
--------------------
Viewset, Modelviewset based views are registered here not at app level but can be done.
#Register views based on viewsets with router
#router.register(r'menuv',views.MenuViewset,basename='menuv')
#router.register(r'bookingv',views.BookingViewset,basename='bookingv')
#Register views based on Modelviewsets with router
#router.register(r'menum',views.MenuModelViewset,basename='menum')
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables',views.BookingModelViewset,basename='table')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),    
    path('restaurant/booking/',include(router.urls)),
]
