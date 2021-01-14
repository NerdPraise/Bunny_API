from rest_framework import serializers


from .models import User, UserTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = '__all__'
