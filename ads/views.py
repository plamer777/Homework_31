"""This unit contains views processing routes such as ad/, ad/1, cat/,
cat/1 and allows to create, update and delete advertisements and categories"""
import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, \
    CreateView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ads, Category, AdsSchema, CategorySchema
from ads.permissions import IsOwnerPermission, IsAdminModerator
from ads.serializers import AdsSerializer
from first_django.settings import ITEMS_PER_PAGE
from users.models import User
# ----------------------------------------------------------------------


def main_page(request):
    """The main page view
    :param request: a request object
    :return: JsonResponse containing a result of the request
    """
    return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(ListView):
    """The AdsView class is a view that serves to work with routes like ad/
    and also provides filtering by category, price, text and location"""
    model = Ads

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        super().get(request, *args, **kwargs)

        cat_list = request.GET.getlist('cat')
        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        text = request.GET.get('text')
        location = request.GET.get('location')
        page = int(request.GET.get('page', 1))

        all_ads = self.object_list.select_related('author').order_by('-price')

        if cat_list:
            all_ads = all_ads.filter(category_id__in=cat_list)
        if text:
            all_ads = all_ads.filter(name__icontains=text)
        if location:
            all_ads = all_ads.filter(author__location__name__icontains=location)
        if price_from and price_to:
            all_ads = all_ads.filter(price__range=(price_from, price_to))

        paginator = Paginator(all_ads, ITEMS_PER_PAGE)
        current_page = paginator.get_page(page)

        ads_list = []
        for ads in current_page:
            current_ads = {'id': ads.id,
                           'author': ads.author.first_name,
                           }
            current_ads.update(AdsSchema.from_orm(ads).dict())
            ads_list.append(current_ads)

        response = {
            'items': ads_list,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }

        return JsonResponse(response, safe=False, json_dumps_params={
            'ensure_ascii': False}, status=200)


class AdsEntityView(RetrieveAPIView):
    """This view serves to display information about a single advertisement"""
    queryset = Ads.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        try:
            ads = self.get_object()
            ads_dict = {'id': ads.id}
            ads_dict.update(AdsSchema.from_orm(ads).dict())
            ads_dict['author'] = ads.author.first_name

            return JsonResponse(ads_dict, safe=False, status=200,
                                json_dumps_params={'ensure_ascii': False})

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class AdsCreateView(CreateView):
    """This view serves to add new advertisement into the database"""
    model = Ads
    fields = ['name', 'author', 'price', 'image', 'description',
              'is_published', 'category']

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process POST requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        ads_data = json.loads(request.body)

        try:
            validated_ads = AdsSchema(**ads_data)
            get_object_or_404(User, pk=validated_ads.author_id)
            get_object_or_404(Category, pk=validated_ads.category_id)
            new_ads = Ads.objects.create(**validated_ads.dict())

            new_ads.save()
            response = {'id': new_ads.id,
                        'author': new_ads.author.first_name}
            response.update(validated_ads.dict())

            return JsonResponse(response, safe=False)

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=422, safe=False)


class AdsUpdateView(UpdateAPIView):
    """This view serves to update existing advertisement"""
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated,
                          IsOwnerPermission | IsAdminModerator]


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DestroyAPIView):
    """This view serves to delete existing advertisement"""
    queryset = Ads.objects.all()
    permission_classes = [IsAuthenticated,
                          IsOwnerPermission | IsAdminModerator]

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process DELETE requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsImageView(UpdateView):
    """This view serves to update existing advertisement's image"""
    model = Ads
    fields = ['name', 'author', 'price', 'image', 'description',
              'is_published', 'category']

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process POST requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        updated_ads = self.get_object()
        file = request.FILES.get('image')
        try:
            updated_ads.image = file
            updated_ads.save()
            response = {
                'id': updated_ads.id,
                'author': updated_ads.author.first_name,
            }
            response.update(AdsSchema.from_orm(updated_ads).dict())

            return JsonResponse(response, status=200)

        except Exception as e:
            return JsonResponse({'error': e}, status=422)
# -------------------------------------------------------------------------


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(ListView):
    """This CBV provides access to categories by the route cat/"""
    model = Category

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        super().get(request, *args, **kwargs)
        all_categories = self.object_list.order_by('name')

        categories_list = []
        for category in all_categories:
            found_category = {'id': category.id}
            found_category.update(CategorySchema.from_orm(category).dict())
            categories_list.append(found_category)

        return JsonResponse(categories_list, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})


class CategoryEntityView(DetailView):
    """This view displays a single category found in the database"""
    model = Category

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        try:
            category = self.get_object()
            category_dict = {'id': category.id}
            category_dict.update(CategorySchema.from_orm(category).dict())
            return JsonResponse(category_dict, safe=False, status=200,
                                json_dumps_params={'ensure_ascii': False})

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    """This view creates a new category by provided data"""
    model = Ads
    fields = ['name']

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process POST requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        category_data = json.loads(request.body)

        try:
            validated_category = CategorySchema(**category_data)
            new_category = Category.objects.create(**validated_category.dict())
            new_category.save()
            response = {'id': new_category.id}
            response.update(validated_category.dict())

            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=422, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    """This view update an existing category"""
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process PATCH requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)

        try:
            validated_category = CategorySchema(**category_data)
            self.object.__dict__.update(validated_category.dict())
            self.object.save()

            return JsonResponse({'id': self.object.id,
                                 'name': self.object.name})
        except Exception as e:
            return JsonResponse({'error': f'{e}'})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    """This view deletes an existing category from the database"""
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=200)
