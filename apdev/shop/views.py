from django.shortcuts import (render, get_object_or_404 as G404)
from apdev.core.classes import (PageElement as pe, PageLoad, ActivePageItems)
from .models import (PageSkin as S, Blog as B, Info as In, Fileserve as F)
from shop.models import Pageitem as P
from apdev.settings import LANGUAGES as L
import pytz
import datetime


# Strona główna.
def home(request):
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    api = ActivePageItems(request, In, pytz, datetime)
    active_infos = api.active_items
    api = ActivePageItems(request, F, pytz, datetime)
    active_files = api.active_items
    context = {
     'blogs': active_blogs,
     'infos': active_infos,
     'files': active_files,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'shop/home.html'
    return render(request, template, context_lazy)
