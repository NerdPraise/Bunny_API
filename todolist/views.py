from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from .models import User, UserTask
from .serializers import UserSerializer, UserTaskSerializer


@api_view(['GET'])
def get_user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    return Response({'message': 'No user is logged in'}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(generics.CreateAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Delete every user
    """
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserTaskRUDAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserTaskSerializer
    queryset = UserTask.objects.all()
    lookup_url_kwarg = 'task_id'
    permission_classes = (IsAuthenticated,)

    def put(self, *args, **kwargs):
        # to allow every user access
        task_id = self.kwargs['task_id']
        try:
            task_instance = UserTask.objects.get(pk=task_id)
            user = task_instance.user_id.pk
        except UserTask.DoesNotExist:
            return Response({'message': 'task doesn\'t exist'})

        data = self.request.data
        data = {**data, 'user_id': user}
        data['description'] = data['description'][0]

        serializer = UserTaskSerializer(task_instance, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTaskCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = UserTaskSerializer
    permission_classes = (IsAuthenticated,)

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
