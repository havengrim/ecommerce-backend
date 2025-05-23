from rest_framework import serializers
from .models import Category, Product, Cart, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # simple category info

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # nested category with name

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'price', 'stock_quantity', 'image_url',
            'description', 'category', 'rating', 'review_count', 'is_new'
        ]
        read_only_fields = ['slug']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_id', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'status', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']