"""This unit contains views processing routes such as ad/, ad/1, cat/, cat/1"""
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from ads.models import AdsModel, CategoryModel, AdsSchema, CategorySchema
# ----------------------------------------------------------------------


def main_page(request):
    """The main page view
    :param request: a request object
    :return: JsonResponse containing a result of the request
    """
    return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(ListView):
    """The AdsView class is a view that serves to work with routes like ad/,
    ad/1"""
    model = AdsModel

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        super().get(request, *args, **kwargs)
        all_ads = self.object_list

        ads_list = []
        for ads in all_ads:
            ads_list.append(AdsSchema.from_orm(ads).dict(exclude={
                'description', 'address', 'is_published'}))

        return JsonResponse(ads_list, safe=False, json_dumps_params={
            'ensure_ascii': False}, status=200)

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process POST requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """

        ads_data = json.loads(request.body)

        try:
            new_ads = AdsModel.objects.create(**ads_data)
            validated_ads = AdsSchema.from_orm(new_ads).dict()
            new_ads.save()
            return JsonResponse(validated_ads, safe=False)

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=422, safe=False)


class AdsEntityView(DetailView):
    """This view serves to display information about a single advertisement"""
    model = AdsModel

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """

        try:
            ads = self.get_object()
            ads_dict = AdsSchema.from_orm(ads).dict()
            return JsonResponse(ads_dict, safe=False, status=200,
                                json_dumps_params={'ensure_ascii': False})

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(ListView):
    """This CBV provides access to categories by the route cat/"""
    model = CategoryModel

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        super().get(request, *args, **kwargs)
        all_categories = self.object_list

        categories_list = []
        for category in all_categories:
            categories_list.append(CategorySchema.from_orm(category).dict())

        return JsonResponse(categories_list, safe=False, status=200,
                            json_dumps_params={'ensure_ascii': False})

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process POST requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """
        category_data = json.loads(request.body)

        try:
            new_category = CategoryModel.objects.create(**category_data)
            validated_category = CategorySchema.from_orm(new_category).dict()
            new_category.save()
            return JsonResponse(validated_category, safe=False, status=200)

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=422, safe=False)


class CategoryEntityView(DetailView):
    """This view displays a single category found in the database"""
    model = CategoryModel

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """This method serves to process GET requests
        :param request: a request object
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: JsonResponse containing a result of the request
        """

        try:
            category = self.get_object()
            category_dict = CategorySchema.from_orm(category).dict()
            return JsonResponse(category_dict, safe=False, status=200,
                                json_dumps_params={'ensure_ascii': False})

        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=404)
