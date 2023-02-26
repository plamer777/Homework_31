from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView
from users.views import UsersView, SingleUserView, CreateUserView, \
    UserUpdateView, DeleteUserView
# --------------------------------------------------------------------------

urlpatterns = [
    path('', UsersView.as_view()),
    path('<int:pk>/', SingleUserView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', DeleteUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
