from rest_framework import generics, status
from rest_framework.response import Response

from .models import User, UserTask
from .serializers import UserSerializer, UserTaskSerializer


class UserAPIView(generics.CreateAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserTaskRUDAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserTaskSerializer
    queryset = UserTask.objects.all()
    lookup_url_kwarg = 'task_id'


class UserTaskCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = UserTaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        qs = UserTask.objects.filter(user_id=user_id)
        return qs

    def post(self, *args, **kwargs):
        user_id = kwargs['user_id']
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User doesn\'t exist'},
                            status=status.HTTP_404_NOT_FOUND)

        data = self.request.data
        data['user_id'] = user.pk

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
