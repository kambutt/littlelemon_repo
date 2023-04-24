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

class MenuView(APIView):
    
    def get(self,request):
        #requires a queryset
        queryset = Menu.objects.all()
        #requires a serializer to convert database data into JSON data
        serializer = MenuSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post (self, request):
        #does not require a queryset
        #POST request has data to be added to database.  First convert it into JSON using serializer made for the model
        serializer = MenuSerializer(data=request.data)
        #Check if the submitted data is valid as per model requirement
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
        

class BookingView(APIView):
    def get(self,request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post (self, request):
        #POST request has data to be added to database.  First convert it into JSON using serializer made for the model
        serializer = BookingSerializer(data=request.data)
        #Check if the submitted data is valid as per model requirement
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
#-----------------------------------------------------------------------------------------------------------------
#API views using viewsets

class MenuViewset(viewsets.ViewSet):
    #Require a queryset
    queryset = Menu.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = MenuSerializer
    #Will apply to all methods
    Permission_classes = [IsAuthenticated]    
    #list instead of get
    def list(self, request):
        #will apply to only this method
        Permission_classes = [IsAuthenticated]
        #Require a queryset
        queryset = self.queryset        
        #Require a serializer to convert the queryset into JSON
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #create instead of post
    def create(self, request):
        #does not require a queryset        
        #Require a serializer to convert the request data into JSON
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data Created'}, status=status.HTTP_201_CREATED)

class BookingViewset(viewsets.ViewSet):
    #Require a queryset
    queryset = Booking.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = BookingSerializer
        
    #list instead of get
    def list(self, request):
        #Require a queryset
        queryset = self.queryset        
        #Require a serializer to convert the queryset into JSON
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #create instead of post
    def create(self, request):
        #does not require a queryset        
        #Require a serializer to convert the request data into JSON
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data Created'}, status=status.HTTP_201_CREATED)
#-------------------------------------------------------------------------------------------------------------------------
#API views using modelviewsets

class MenuModelViewset(viewsets.ModelViewSet):
    #Require a queryset
    queryset = Menu.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = MenuSerializer
        
    #list instead of get
    def list(self, request):
        #Require a queryset
        queryset = self.queryset        
        #Require a serializer to convert the queryset into JSON
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #create instead of post
    def create(self, request):
        #does not require a queryset        
        #Require a serializer to convert the request data into JSON
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data Created'}, status=status.HTTP_201_CREATED)

class BookingModelViewset(viewsets.ModelViewSet):
    #Require a queryset
    queryset = Booking.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = BookingSerializer
    #Queryset and serializer class provides basic CRUD operational capability on its own.
    #Definining further functions is for customization.    
    """
    def list(self, request):
        #Require a queryset
        queryset = self.queryset        
        #Require a serializer to convert the queryset into JSON
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #create instead of post
    def create(self, request):
        #does not require a queryset        
        #Require a serializer to convert the request data into JSON
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data Created'}, status=status.HTTP_201_CREATED)
    """
#--------------------------------------------------------------------------------------------------
#API Views using Generic views        

class MenuGenericView(generics.ListCreateAPIView):
    #Require a queryset
    queryset = Menu.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = MenuSerializer
        
    #list instead of get
    def list(self, request):
        #Require a queryset
        queryset = self.get_queryset()       
        #Require a serializer to convert the queryset into JSON
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #create instead of post
    def create(self, request):
        #does not require a queryset        
        #Require a serializer to convert the request data into JSON
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data Created'}, status=status.HTTP_201_CREATED)

class BookingGenericView(generics.ListCreateAPIView):
    #Require a queryset
    queryset = Booking.objects.all()
    #Require a serializer to convert the queryset into JSON
    serializer_class = BookingSerializer
        
    #list instead of get
    def list(self, request):
        #Require a queryset
        queryset = self.get_queryset()
        #Require a serializer to convert the queryset into JSON
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #create instead of post
    def create(self, request):
        #does not require a queryset        
        #Require a serializer to convert the request data into JSON
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data Created'}, status=status.HTTP_201_CREATED)
#------------------------------------------------------------------------------------------------------------
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
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