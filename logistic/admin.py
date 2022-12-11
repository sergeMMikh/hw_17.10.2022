from django.contrib import admin

from .models import Product, StockProduct, Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    ...
