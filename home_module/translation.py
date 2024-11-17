from modeltranslation.translator import TranslationOptions,register
from .models import Product


@register(Product)
class ProductTranslationOption(TranslationOptions):
    fields = ['title']