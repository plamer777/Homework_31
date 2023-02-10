"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ads.views import CategoryView, AdsView, CategoryEntityView, \
    AdsEntityView, AdsCreateView, CategoryCreateView, AdsUpdateView, \
    CategoryUpdateView, AdsDeleteView, CategoryDeleteView, AdsImageView
# --------------------------------------------------------------------------

urlpatterns = [
    path('cat/', CategoryView.as_view()),
    path('ad/', AdsView.as_view()),
    path('ad/<int:pk>/', AdsEntityView.as_view()),
    path('cat/<int:pk>/', CategoryEntityView.as_view()),
    path('ad/create/', AdsCreateView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('ad/<int:pk>/update/', AdsUpdateView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdsDeleteView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdsImageView.as_view()),
]
