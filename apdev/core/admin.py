from django.contrib import admin
from .models import User, Pageitem, PageSkin

# Register your models here.
admin.site.register(User)
admin.site.register(Pageitem)
admin.site.register(PageSkin)
