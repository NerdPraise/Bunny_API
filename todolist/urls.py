from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (UserAPIView, UserListView,
                    UserTaskRUDAPIView, UserTaskCreateListAPIView)

app_name = 'todolist'
urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/create/', UserAPIView.as_view(), name='user-create'),
    path('user/<int:user_id>', UserAPIView.as_view(),
         name='user-retrieve-update-delete'),

    # User Task
    path('task/<int:user_id>/',
         UserTaskCreateListAPIView.as_view(), name='task-create-list'),

    path('tasks/<int:task_id>/', UserTaskRUDAPIView.as_view(),
         name='task-retrieve-update-delete'),

    path('auth/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
