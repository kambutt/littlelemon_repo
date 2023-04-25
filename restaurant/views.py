from django.shortcuts import render
from django.http import HttpResponse

#For APIs
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

#For APIs using viewsets
from rest_framework import viewsets
from rest_framework import status

#For APIs using Generic views
from rest_framework import generics

#For authentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#API views for models based on their serializers

class BookingModelViewset(viewsets.ModelViewSet):
    #Require a queryset
    queryset = Booking.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = BookingSerializer
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    #comment the following line before running test otherwise the test will fail authentication
    permission_classes = [IsAuthenticated]
    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Data Created'},status=status.HTTP_201_CREATED)

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
#----------------------------------------------------------------------------------------------------------------
#Implementation of Token authentication using Function based views
#This decorator turns the function based view into an API view
@api_view()
#This decorated implements the Token authentication registered in settings.py file.
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})