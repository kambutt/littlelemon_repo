from django.test import TestCase
from .models import Menu

from django.urls import reverse
from rest_framework.test import APIClient

#function to create a database record in Menu model
def create_menutestitem(title, price, inventory):
    testmenuitem = []
    newitem = Menu.objects.create(title=title, price=price, inventory =inventory)
    testmenuitem.append(newitem)
    return testmenuitem

class MenuItemViewTest(TestCase):
    
    def setUp(self):
        self.client =APIClient()
        #Call to above function to create a database record in menu model
        self.testmenuitems = create_menutestitem("Ice Cream", 5.99, 30)
    
    def test_getall(self):
        #getting url that uses the View to be tested i.e. MenuItemView using name value given in urls.py
        url = reverse("menu")        
        #query the database using the APIView from urls.py
        response = self.client.get(url)
        #Check if it worked
        self.assertEqual(response.status_code, 200)
        #Retrieve the test record that was created
        added_menuitem = self.testmenuitems
        #Retrieve the query data received from Url call to the APIView
        expected_menuitem = response.data
        #Check if both are the same.  Created 1 record, query provided 1 record
        self.assertEqual(len(added_menuitem), len(expected_menuitem))
        for i in range (len(expected_menuitem)):
            #Get single records.  Looping in case multiple records are created for testing in setUp
            menuadd = added_menuitem[i]
            menuexp = expected_menuitem[i]
            #Match created versus queried data
            self.assertEqual(menuadd.title, menuexp['title'])
            self.assertEqual(str(menuadd.price), menuexp['price'])
