from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemsViewTest(TestCase):
    def setUp(self):
        Menu.objects.bulk_create([
            Menu(title="Ice cream", price=2, inventory=100),
            Menu(title="Cheese cake", price=6, inventory=10),
            Menu(title="Lemon pie", price=5, inventory=20)
        ])
        
    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        expected_data = [
            {
                'id': 1,
                'title': "Ice cream", 
                'price': "2.00",
                'inventory': 100
            },
            {
                'id': 2,
                'title': "Cheese cake", 
                'price': "6.00",
                'inventory': 10
            },
            {
                'id': 3,
                'title': "Lemon pie", 
                'price': "5.00",
                'inventory': 20
            },
        ]
        
        serialized_items_data = sorted(serialized_items.data, key=lambda x: x['title'])
        expected_data = sorted(expected_data, key=lambda x: x['title'])
        
        self.assertEqual(serialized_items_data, expected_data)