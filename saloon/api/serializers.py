from rest_framework import serializers
from saloon.models import *

class WebImageSerializer(serializers.ModelSerializer):
    src = serializers.ImageField()

    class Meta:
        model = WebImage
        fields = ("src", ) 

class MobileImageSerializer(serializers.ModelSerializer):
    src = serializers.ImageField()

    class Meta:
        model = MobileImage
        fields = ("src", ) 



class ServicesSerializer(serializers.ModelSerializer):
    web_images = WebImageSerializer(many=True)
    mobile_images = MobileImageSerializer(many=True)
    class Meta:
        model = Services
        exclude = ['created_at', 'updated_at', 'views', 'is_active', 'company']

class WorkersSerializer(serializers.ModelSerializer):
    web_images = WebImageSerializer(many=True)
    mobile_images = MobileImageSerializer(many=True)
    class Meta:
        model = Workers
        exclude = ['created_at', 'updated_at', 'views', 'is_active', 'company']

class CompanySerializer(serializers.ModelSerializer):
    web_images = WebImageSerializer(many=True)
    mobile_images = MobileImageSerializer(many=True)
    workers = WorkersSerializer(many=True, read_only=True)
    services = ServicesSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__p'