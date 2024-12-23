from rest_framework import serializers
from .models import *

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Serializer for Sale model
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
# Serializer for Sale model
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# Serializer for Sale model
class CustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# Serializer for Sale model
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
