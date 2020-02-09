from modeltranslation.translator import translator, TranslationOptions
from .models import Offer, Info, Service


class OfferTranslate(TranslationOptions):
    fields = ('title', 'body', )


translator.register(Offer, OfferTranslate)


class InfoTranslate(TranslationOptions):
    fields = ('title', 'body', )


translator.register(Info, InfoTranslate)


class ServiceTranslate(TranslationOptions):
    fields = ('title', 'body', )


translator.register(Service, ServiceTranslate)
