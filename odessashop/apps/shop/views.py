from django.db.models.query import QuerySet
from rest_framework.views import APIView
from apps.utils.customClasses import (
    SellersPagination,
    CardFilter,
)
from rest_framework.filters import OrderingFilter
from apps.utils.func import order_queryset, order_queryset_by_dynamic_params
from .models import (
    Category,
    Card,
    Shop,
)
from .serializers import (
    CategoryGetSerializer,
    CardCreateSerializer,
    ShortShopSerializer,
    CardGetSerializer,
    ShopCreateSerializer,
    ShopPartialUpdateSerializer,
    CardPartialUpdateSerializer,
)
import logging
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView


class CardFilteredAPI(generics.ListAPIView):
    permissions = permissions.AllowAny,
    queryset = Card.objects.all()
    filterset_class = CardFilter
    serializer_class = CardGetSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        params = dict(self.request.query_params)
        order_params = [value for key,
                        value in params.items() if key.startswith('order')]
        dynamic_order_params = [value for key,
                                value in params.items() if key.startswith('dynamic_order')]
        if order_params:
            queryset = order_queryset(queryset, order_params[0])
        if dynamic_order_params:
            queryset = order_queryset_by_dynamic_params(
                queryset, dynamic_order_params[0])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryListAPI(generics.ListAPIView):
    permissions = permissions.AllowAny,
    queryset = Category.objects.all()
    serializer_class = CategoryGetSerializer
    filterset_class = CardFilteredAPI


class CardGetAPI(generics.RetrieveAPIView):
    permissions = permissions.AllowAny,
    queryset = Card.objects.all()
    serializer_class = CardGetSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CardCreateAPI(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CardPartialUpdateAPI(GenericAPIView, UpdateModelMixin):
    queryset = Card.objects.all()
    serializer_class = CardPartialUpdateSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ShopCreateAPI(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CardDeleteAPI(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardCreateSerializer


class ShopDeleteAPI(generics.DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopCreateSerializer


class ShopGetAPI(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShortShopSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ShopPartialUpdateAPI(GenericAPIView, UpdateModelMixin):
    queryset = Shop.objects.all()
    serializer_class = ShopPartialUpdateSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ShopsGetByCategory(GenericAPIView):
    serializer_class = ShortShopSerializer
    queryset = Shop.objects.all()

    def get(self, request, category_id):
        queryset = Shop.objects.filter(category__pk=category_id)
        return Response(self.serializer_class(instance=queryset, many=True).data)


class ShopsGetByUsername(GenericAPIView):
    serializer_class = ShortShopSerializer
    queryset = Shop.objects.all()

    def get(self, request, username: str):
        queryset = Shop.objects.filter(owner=username)
        return Response(self.serializer_class(instance=queryset, many=True).data)
