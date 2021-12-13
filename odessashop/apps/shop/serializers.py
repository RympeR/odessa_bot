from rest_framework import serializers
from django.db.models import Avg, Count
from apps.utils.customFields import TimestampField
from .models import (
    Category,
    Card,
    Shop,
    Attachment,
)
from random import sample


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = '__all__'


class CategoryGetSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Category.objects.all(),)

    class Meta:
        model = Category
        fields = '__all__'

    def get_category_image(self, category):
        request = self.context.get('request')
        if category.category_image and getattr(category.category_image, 'url'):
            file_url = category.category_image.url
            return request.build_absolute_uri(file_url)
        return None

class CardCreateSerializer(serializers.ModelSerializer):

    seller = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Shop.objects.all())
    discount_price = serializers.FloatField(required=False)

    class Meta:
        model = Card
        fields = '__all__'


class ShortShopSerializer(serializers.ModelSerializer):
    products_amount = serializers.SerializerMethodField()

    def get_products_amount(self, shop):
        return len(shop.card_creator.all())

    class Meta:
        model = Shop
        exclude = 'description',


class CardGetSerializer(serializers.ModelSerializer):
    seller = ShortShopSerializer()
    category = CategoryGetSerializer()
    attachments = AttachmentSerializer(many=True)

    def get_preview(self, card):
        request = self.context.get('request')
        if card.preview and getattr(card.preview, 'url'):
            file_url = card.preview.url
            return request.build_absolute_uri(file_url)
        return None

    class Meta:
        model = Card
        fields = (
            'pk',
            'title',
            'description',
            'seller',
            'present',
            'price',
            'preview',
            'attachments',
            'category',
            'time_creation',
        )


class ShopCreateSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)

    class Meta:
        model = Shop
        fields = '__all__'


class ShopPartialUpdateSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    logo = serializers.ImageField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Shop
        fields = '__all__'


class CardPartialUpdateSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    seller = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Shop.objects.all())
    present = serializers.BooleanField(required=False)
    price = serializers.FloatField(required=False)
    preview = serializers.ImageField(required=False)
    category = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Category.objects.all())

    time_creation = serializers.DateTimeField(required=False)
    attachments = serializers.PrimaryKeyRelatedField(
        required=False, many=True, queryset=Attachment.objects.all())

    class Meta:
        model = Card
        fields = '__all__'
