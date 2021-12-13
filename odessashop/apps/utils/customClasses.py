from apps.shop.models import Card, Category
from apps.shop.serializers import CategoryGetSerializer
from django.db.models import Q, Model, QuerySet
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import ModelSerializer


def filter_related_objects(queryset: QuerySet, name: str, value, model: Model, serializer: ModelSerializer, related_category: str) -> QuerySet:
    lookup = '__'.join([name, 'in'])
    res = []
    if value:
        subjects = model.objects.filter(pk__in=[obj.pk for obj in value])
        look_related = '__'.join([related_category, 'gte'])
        result = []
        for subj in subjects:
            hole_tree = model.objects.filter(
                Q(tree_id=subj.tree_id) &
                Q(**{look_related: getattr(subj, related_category)}) &
                Q(display=True)
            )
            values = [serializer(
                instance=subject).data['id'] for subject in hole_tree]
            result.append(values)
        values = result
    else:
        subjects = model.objects.filter(display=True)
        values = [serializer(
            instance=subject).data['id'] for subject in subjects]
    for value in values:
        if isinstance(value, list):
            res.extend(value)
        else:
            res.append(value)

    return queryset.filter(**{lookup: res}).distinct().order_by('id')


class SellersPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100


class CardFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr='gte')
    title = filters.CharFilter(lookup_expr='icontains')
    seller = filters.CharFilter(lookup_expr='icontains')
    price = filters.RangeFilter(lookup_expr='range')
    category = filters.ModelMultipleChoiceFilter(
        lookup_expr='in',
        queryset=Category.objects.all(),
        field_name='category',
        method='filter_category'
    )
    present = filters.BooleanFilter()
    time_creation = filters.DateTimeFromToRangeFilter(lookup_expr='range')

    def filter_category(self, queryset: QuerySet, name: str, value):
        return filter_related_objects(queryset, name, value, Category, CategoryGetSerializer, 'subcategory')

    class Meta:
        model = Card
        fields = (
            'id',
            'title',
            'seller',
            'price',
            'present',
            'category',
        )
