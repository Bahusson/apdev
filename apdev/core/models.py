from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


# Klasa zmienia autentykację Usera na email jak w Core2.
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


# Klasa Głównych Elementów Strony
class Pageitem(models.Model):
    lang_flag = models.ImageField(upload_to='images')  # Mały obrazek języka
    headtitle = models.CharField(max_length=200)  # Nagłówek strony w tym j
    mainpage = models.CharField(max_length=200)  # Strona główna w tym języku
    aboutus = models.CharField(max_length=200)  # Informacje w tym języku
    offer = models.CharField(max_length=200)  # Mapa akademików w tym języku
    contact = models.CharField(max_length=200)  # Kontakty w tym języku
    gallery = models.CharField(max_length=200)  # Galeria
    main_intro = models.TextField()  # Długie info na głównej
    about_intro = models.TextField()  # Długie info na "o nas"
    save_time = models.CharField(max_length=200)  # oszczędzaj czas
    cookie_alert = models.CharField(max_length=200)  # ciastki
    location = models.CharField(max_length=200)  # lokalizacja

    def mainpage_c(self):
        return self.mainpage.upper()


# Klasa skórek do apki. Pola nienulowalne.
class PageSkin(models.Model):
    themetitle = models.CharField(max_length=200)
    position = models.IntegerField()
    offerimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    infoimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    serviceimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    fileimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    logo_main = models.ImageField(
     upload_to='skins', blank=True, null=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.themetitle
