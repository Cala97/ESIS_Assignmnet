from store.models import Product , OrderItem , ShippingAddress , FullOrder , Purchased_item
from store.models import ProductCategories
from rest_framework import serializers


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullOrder
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        exclude = ['user']

    def create(self, validated_data):
        return ShippingAddress.objects.create(**validated_data)

    def update(self, instance, validated_data):

        for field in ['recipient_fullname', 'phone_no', 'address_line1', 'address_line2', 'city', 'state', 'country', 'zipcode']:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()
        return instance



