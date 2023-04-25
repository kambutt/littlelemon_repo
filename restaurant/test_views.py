from django.test import TestCase
from .models import Menu

from django.urls import reverse
from rest_framework.test import APIClient

def create_menutestitem(title, price, inventory):
    testmenuitem = []
    newitem = Menu.objects.create(title=title, price=price, inventory =inventory)
    testmenuitem.append(newitem)
    return testmenuitem

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client =APIClient()
        self.testmenuitems = create_menutestitem("Ice Cream", 5.99, 30)
    
    def test_getall(self):
        url = reverse("menu")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        added_menuitem = self.testmenuitems
        expected_menuitem = response.data
        self.assertEqual(len(added_menuitem), len(expected_menuitem))
        for i in range (len(expected_menuitem)):
            menuadd = added_menuitem[i]
            menuexp = expected_menuitem[i]
            self.assertEqual(menuadd.title, menuexp['title'])
            self.assertEqual(str(menuadd.price), menuexp['price'])
