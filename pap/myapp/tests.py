from django.test import TestCase
from .models import Cashflow, Product, AffordabilityPrediction
from django.urls import reverse
from django.core.paginator import Paginator

class CashflowModelTest(TestCase):
    def setUp(self):
        self.cashflow = Cashflow.objects.create(date='2024-01-01', income=1000, expenses=500)

    def test_cashflow_creation(self):
        self.assertEqual(self.cashflow.income, 1000)
        self.assertEqual(self.cashflow.expenses, 500)

    def test_cashflow_view(self):
        response = self.client.get(reverse('cashflow_list'))
        self.assertEqual(response.status_code, 200)

    def test_cashflow_pagination(self):
        for i in range(30): 
            Cashflow.objects.create(date='2024-01-01', income=1000, expenses=500)
        response = self.client.get(reverse('cashflow_list'), {'page': 2})
        self.assertEqual(response.status_code, 200)

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Laptop', price=1200)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Laptop')
        self.assertEqual(self.product.price, 1200)

    def test_product_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_pagination(self):
        for i in range(30):  
            Product.objects.create(name=f'Product {i}', price=100 + i)
        response = self.client.get(reverse('product_list'), {'page': 2})
        self.assertEqual(response.status_code, 200)

class AffordabilityPredictionTest(TestCase):
    def setUp(self):
        self.cashflow = Cashflow.objects.create(date='2024-01-01', income=1000, expenses=500)
        self.product = Product.objects.create(name='Laptop', price=1200)
        self.prediction = AffordabilityPrediction.objects.create(cashflow=self.cashflow, product=self.product, predicted_affordability=600)

    def test_prediction_creation(self):
        self.assertEqual(self.prediction.predicted_affordability, 600)

    def test_affordability_prediction_view(self):
        response = self.client.get(reverse('affordability_predictions'))
        self.assertEqual(response.status_code, 200)

    def test_affordability_pagination(self):
        for i in range(30):  
            AffordabilityPrediction.objects.create(
                cashflow=self.cashflow,
                product=self.product,
                predicted_affordability=600 + i
            )
        response = self.client.get(reverse('affordability_predictions'), {'page': 2})
        self.assertEqual(response.status_code, 200)
