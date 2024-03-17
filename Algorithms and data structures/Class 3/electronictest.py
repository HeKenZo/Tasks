import unittest
import csv
from electronics import clean_data, save_to_csv

class TestElectronicsFunctions(unittest.TestCase):
    def setUp(self):
        self.data = [
            {
                "id": "1",
                "name": "Product 1",
                "category": "Appliances",
                "price": 320.46,
                "currency": "USD",
                "stock": 51,
                "description": "Description of product 1",
                "manufacturer": "CamTech",
                "warranty": "2 years",
                "extra_field": None
            },
            {
                "id": "2",
                "name": "Product 2",
                "category": "Wearables",
                "price": 808.81,
                "currency": "USD",
                "stock": 127,
                "description": "Description of product 2",
                "manufacturer": "BrightLife",
                "warranty": "1 year",
                "extra_field": "Extra value 2"
            },
            {
                "id": "3",
                "name": "Product 3",
                "category": "Cleaning",
                "price": 467.24,
                "currency": "USD",
                "stock": 122,
                "description": "Description of product 3",
                "manufacturer": "TabTech",
                "warranty": "2 years",
                "extra_field": "Extra value 3"
            }
        ]

    def test_clean_data(self):
        cleaned_data = clean_data(self.data)
        for product in cleaned_data:
            self.assertIsInstance(product['price'], float)
            if product['stock'] is not None:
                self.assertIsInstance(product['stock'], int)

    def test_save_to_csv(self):
        csv_file_path = 'test_electronics_products_cleaned.csv'
        save_to_csv(self.data, csv_file_path)

        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertTrue(row['id'])
                self.assertTrue(row['name'])
                self.assertTrue(row['category'])
                self.assertTrue(row['price'])
                self.assertTrue(row['currency'])
                self.assertTrue(row['stock'])
                self.assertTrue(row['description'])
                self.assertTrue(row['manufacturer'])
                self.assertTrue(row['warranty'])


if __name__ == '__main__':
    unittest.main()
