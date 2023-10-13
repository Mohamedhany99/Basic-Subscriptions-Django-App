from rest_framework import serializers
from .models import CustomUser, Package, Subscription


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"
        ordering = "price"


class SubscriptionSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = ["id", "user", "packages", "timestamp"]
