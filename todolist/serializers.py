from rest_framework import serializers


from .models import User, UserTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active')

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = '__all__'
