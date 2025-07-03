from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'price', 'stock_quantity', 'image_url', 
            'description', 'category', 'rating', 'review_count', 'is_new'
        ]
        read_only_fields = ['slug']  # slug is auto-generated, not set by user
