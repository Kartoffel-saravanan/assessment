from rest_framework import serializers
from database.models import Account, Destination


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwarg = {
            'account_id': {'write_only': True, 'read_only': True, 'required': True},
            'email': {'write_only': True, 'read_only': True, 'required': True},
            'account_name': {'read_only': True, 'write_only': True, 'required': True},
        }

    def create(self, validated_data):
        return Account.objects.create(**validated_data)


class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        extra_kwarg = {
            'urls': {'write_only': True, 'read_only': True, 'required': True},
            'http_methods': {'write_only': True, 'read_only': True, 'required': True},
            'headers': {'read_only': True, 'write_only': True, 'required': True},
        }

    def create(self, validated_data):
        return Destination.objects.create(**validated_data)


class UpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.account_id = validated_data.get('account_id', instance.account_id)
        instance.email = validated_data.get('email', instance.email)
        instance.account_name = validated_data.get('account_name', instance.account_name)
        instance.save()
        return instance
