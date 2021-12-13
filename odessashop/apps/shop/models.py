from django.db import models
from django.core import validators
from django.db.models import CheckConstraint, F, Q
from django.db.models.aggregates import Avg, Count
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from unixtimestampfield.fields import UnixTimeStampField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from apps.utils.func import attachments, preview_cards


FILE_TYPES = (
    ('image', 'image'),
    ('video', 'video'),
    ('audio', 'audio'),
)

class Attachment(models.Model):
    attachment = models.FileField("Файл", null=True, blank=True)
    attachment_type = models.CharField(
        'Тип файла', null=False, default='image', max_length=15, choices=FILE_TYPES)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'


class Shop(models.Model):
    owner = models.CharField('User', max_length=255)
    name = models.CharField(max_length=255, verbose_name='Название')
    logo = ProcessedImageField(
        verbose_name='Логотип',
        upload_to=preview_cards,
        processors=[ResizeToFill(120, 120)],
        options={'quality': 100})
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True)

    def admin_preview(self):
        if hasattr(self.logo, 'url') and self.logo:
            return mark_safe('<img src="{}" width="100" /'.format(self.logo.url))
        return None

    def average_rate(self):
        return (
            self.shop_rate.all().aggregate(Avg('rate')).get(
                'rate__avg', 0) if self.shop_rate.all() else 0
        )

    admin_preview.short_description = 'Превью'
    admin_preview.allow_tags = True

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f"{self.name}"


class Category(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='parent_category', blank=True, null=True, related_name='parent_category', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=100)
    display = models.BooleanField('Отобразить', default=True)
    category_image = models.ImageField(
        verbose_name='Картинка категории', blank=True, null=True)

    def admin_preview(self):
        if self.category_image and hasattr(self.category_image, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.category_image.url))
        return None

    admin_preview.short_description = 'Превью'
    admin_preview.allow_tags = True

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'subcategory'

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Card(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание товара', null=True, blank=True)
    seller = models.ForeignKey(
        Shop, related_name='card_creator', verbose_name='Магазин продавца', on_delete=models.CASCADE,)
    present = models.BooleanField(default=True, verbose_name='В наличии')
    price = models.FloatField(verbose_name='Цена')
    preview = ProcessedImageField(upload_to=preview_cards,
                                  processors=[ResizeToFill(100, 100)],
                                  options={'quality': 100})
    category = models.ForeignKey(
        Category, related_name='card_category', verbose_name='Категория товара', null=True, on_delete=models.SET_NULL,)
    time_creation = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    attachments = models.ManyToManyField(
        Attachment, related_name='card_attachments', verbose_name='Вложения')
        
    def admin_preview(self):
        if hasattr(self.preview, 'url') and self.preview:
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    admin_preview.short_description = 'Превью'
    admin_preview.allow_tags = True

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
