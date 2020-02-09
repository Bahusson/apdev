from django.shortcuts import (render, get_object_or_404 as G404)
from core.classes import (PageElement as pe, PageLoad, ActivePageItems)
#from apdev.core import (PageSkin as S, Pageitem as P)
#from .models import (Offer as O, Info as In, Fileserve as F)
from apdev.settings import LANGUAGES as L
import pytz
import datetime


# Strona główna.
def home(request):
    api = ActivePageItems(request, O, pytz, datetime)
    active_offers = api.active_items
    api = ActivePageItems(request, In, pytz, datetime)
    active_infos = api.active_items
    api = ActivePageItems(request, F, pytz, datetime)
    active_files = api.active_items
    context = {
     'offers': active_offers,
     'infos': active_infos,
     'files': active_files,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'shop/home.html'
    return render(request, template, context_lazy)
