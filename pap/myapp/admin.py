from django.contrib import admin
from .models import Cashflow, Product, AffordabilityPrediction

@admin.register(Cashflow)
class CashflowAdmin(admin.ModelAdmin):
    list_display = ['date', 'income', 'expenses']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(AffordabilityPrediction)
class AffordabilityPredictionAdmin(admin.ModelAdmin):
    list_display = ['cashflow', 'product', 'predicted_affordability']
