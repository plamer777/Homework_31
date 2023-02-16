from django.urls import path
from users.views import UsersView, SingleUserView, CreateUserView, \
    UserUpdateView, DeleteUserView
# --------------------------------------------------------------------------

urlpatterns = [
    path('user/', UsersView.as_view()),
    path('user/<int:pk>/', SingleUserView.as_view()),
    path('user/create/', CreateUserView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', DeleteUserView.as_view()),
]
