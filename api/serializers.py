from rest_framework import serializers
from base.models import Account, Product, RequestForm
from django.contrib.auth.models import User

# account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '___all__'


class AccountDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email',
                  'password')

# product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user
# gửi yêu cầu đến admin


class RequestFormSerializer(serializers.RequestForm):
    class Meta:
        model = RequestForm
        fields = '__all__'
