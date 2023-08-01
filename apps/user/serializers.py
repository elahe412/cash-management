from rest_framework import serializers

from apps.user.models import CustomUser, Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def is_valid(self, raise_exception=False):
        result = super().is_valid(raise_exception=False)
        if not self.errors.get('errors'):
            self.validate(self.initial_data)
        return super().is_valid(raise_exception)

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.set_password(validated_data['password'])
        obj.save()
        return obj


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'id', 'created_at', 'is_staff']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'balance']

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer()
        return super().to_representation(instance)
