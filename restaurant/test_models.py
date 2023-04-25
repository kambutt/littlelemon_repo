from django.test import TestCase
from .models import Menu

#Extend the django testcases.textcase class for Menu Model
class MenuTest(TestCase):
    
    def test_get_item(self):
        #Create an instance of the Menu i.e. record of Menu Item table
        item = Menu.objects.create(title="Ice Cream", price=20, inventory = 30)
        #Now test if the the above statment did its job and see if the record was created accurately by matching it with the specified values.        
        self.assertEqual(str(item),"Ice Cream : 20")
        
        
    