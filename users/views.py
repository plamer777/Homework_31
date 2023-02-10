"""This unit contains CBVs to get user's data from the database"""
import json
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from users.models import User, Location, UserSchema
from first_django.settings import ITEMS_PER_PAGE
# -------------------------------------------------------------------------


class UsersView(ListView):
    """
    A ListView class to handle the request for a list of users.
    """
    model = User

    def get(self, request, *args, **kwargs):
        """
        Handles the GET request for a list of users.
        :param request: the request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        Returns:
            JsonResponse: A JSON response containing the list of users.
        """
        super().get(request, *args, **kwargs)
        page = int(request.GET.get('page', 1))

        self.object_list = self.object_list.annotate(
            total_ads=Count('ads', filter=Q(
                ads__is_published=True))).select_related(
            'location').order_by('username')

        paginator = Paginator(self.object_list, ITEMS_PER_PAGE)
        users_page = paginator.get_page(page)

        users_list = []
        for user in users_page:
            user_dict = {'id': user.id}
            user_dict.update(UserSchema.from_orm(user).dict(exclude={
                'password'}))
            user_dict['total_ads'] = user.total_ads
            user_dict['location'] = user_dict['location'].split(', ')

            users_list.append(user_dict)

        response = {
            'items': users_list,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }

        return JsonResponse(response, safe=False, status=200)


class SingleUserView(DetailView):
    """
    A DetailView class to handle the request for a single user.
    """
    model = User

    def get(self, request, *args, **kwargs):
        """
        Handles the GET request for a single user.
        :param request: the request object
        :param args: positional arguments
        :param kwargs: keyword arguments

        Returns:
            JsonResponse: A JSON response containing the requested user's
            information.
        """
        user = self.get_object()

        response = {'id': user.id}
        response.update(UserSchema.from_orm(user).dict())
        response['location'] = response['location'].split(', ')

        return JsonResponse(response, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(CreateView):
    """
    View to create a new user instance
    """
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role',
              'age', 'location']

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request for creating a user instance

        :param request: The request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: A JsonResponse containing the details of the created user
        instance
        """
        user_data = json.loads(request.body)

        try:
            validated_data = UserSchema(**user_data).dict()

            loc_str = ', '.join(validated_data['location'])
            location, _ = Location.objects.get_or_create(
                name=loc_str, defaults={'lat': 55.738472, 'lng': 37.610953})
            validated_data['location'] = location

            new_user = User.objects.create(**validated_data)
            new_user.save()

            validated_data['location'] = loc_str.split(', ')
            validated_data.pop('password')

            response = {'id': new_user.id}
            response.update(validated_data)

            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=422)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    """
    View to update a user instance
    """
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role',
              'age', 'location']

    def patch(self, request, *args, **kwargs):
        """
        Handle the PATCH request for updating a user instance

        :param request: The request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: A JsonResponse containing the updated details of the user
        instance
        """
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)
        try:
            validated_data = UserSchema(**user_data).dict(exclude_none=True)
            validated_data.pop('role')
            if 'location' in validated_data:
                location, _ = Location.objects.get_or_create(
                    name=validated_data['location'], defaults={
                        'lat': 55.751275, 'lng': 37.610953})
                self.object.location = location

            self.object.__dict__.update(validated_data)
            self.object.save()

            response = {'id': self.object.id}
            response.update(UserSchema.from_orm(self.object).dict(exclude={
                'password', 'role'}))
            response['location'] = self.object.location.name.split(', ')

            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=422)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteUserView(DeleteView):
    """
    View to delete a user instance from the database
    """
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
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

        return JsonResponse({'status': 'ok'}, status=200)
