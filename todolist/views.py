from rest_framework import generics

from .serializers import UserSerializer, UserTaskSerializer


class UserAPIView(generics.CreateAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer


class UserTaskAPIView(generics.CreateAPIView):
    serializer_class = UserTaskSerializer
