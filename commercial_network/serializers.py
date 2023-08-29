from rest_framework import serializers
from .models import Supplier, NetworkNode, Product


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt',)


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
