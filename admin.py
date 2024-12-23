from django.contrib import admin
from .models import Product, Customer, Supplier, Order, Sale

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Sale)
