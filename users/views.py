"""This unit contains CBVs to get and add user's data from/to the database"""
from django.db.models import Count, Q
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView
from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer, \
    UserCreateSerializer, UserUpdateSerializer
# -------------------------------------------------------------------------


class UsersView(ListAPIView):
    """
    A ListView class to handle the request for a list of users.
    """
    queryset = User.objects.annotate(total_ads=Count('ads', filter=Q(
                ads__is_published=True))).select_related(
            'location').order_by('username')
    serializer_class = UserListSerializer


class SingleUserView(RetrieveAPIView):
    """
    A DetailView class to handle the request for a single user.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class CreateUserView(CreateAPIView):
    """
    View to create a new user instance
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """
    View to update a user instance
    """
    queryset = User
    serializer_class = UserUpdateSerializer


class DeleteUserView(DestroyAPIView):
    """
    View to delete a user instance from the database
    """
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        """
        Handle the DELETE request for deleting a user instance from the
        database

        :param request: The request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: A JsonResponse containing the updated details of the user
        instance
        """
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'deleted successfully'}, status=200)
