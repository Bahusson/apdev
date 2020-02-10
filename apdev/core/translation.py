from modeltranslation.translator import translator, TranslationOptions
from .models import Pageitem


class PageitemTranslate(TranslationOptions):
    fields = (
     'lang_flag', 'headtitle', 'mainpage', 'aboutus', 'offer', 'contact',
     'gallery', 'main_intro', 'about_intro', 'save_time', 'cookie_alert',
     'location')


translator.register(Pageitem, PageitemTranslate)
