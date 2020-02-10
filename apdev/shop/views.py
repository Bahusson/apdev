from django.shortcuts import (render, get_object_or_404 as G404)
from core.classes import (PageElement as pe, PageLoad, ActivePageItems)
from core.models import (PageSkin as S, Pageitem as P)
from .models import (Offer as Of, Info as In, Service as Se)
from apdev.settings import LANGUAGES as L
import pytz
import datetime


# Strona główna.
def home(request):
    api = ActivePageItems(request, Of, pytz, datetime)
    active_offers = api.active_items
    api = ActivePageItems(request, In, pytz, datetime)
    active_infos = api.active_items
    api = ActivePageItems(request, Se, pytz, datetime)
    active_services = api.active_items
    context = {
     'offers': active_offers,
     'infos': active_infos,
     'services': active_services,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'shop/home.html'
    return render(request, template, context_lazy)
