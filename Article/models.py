# coding=utf-8
from django.contrib.auth.models import User

__author__ = 'mehmet'

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


"""
Area Adres bilgisi için iülke bilgisini içerir.
    name = ülke ismi.
    cdate = Satırın oluşturulma tarihi.
"""


class Area(models.Model):
    name = models.CharField(max_length=20, default='', null=False, blank=False)
    cdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


"""
Cities Adres bilgisi için il bilgisini içerir.
    name = Şehir ismi.
    cdate = Satırın oluşturulma tarihi
"""


class Cities(models.Model):
    name = models.CharField(max_length=15, default='', null=False, blank=False)
    area = models.ForeignKey(Area, null=True, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


"""
Countinies Adres bilgisi için ilçe bilgisini içerir.
    name = İlçe Adı.
    city = İlçenin bağlı olduğu il.
    cdate = Satırın oluşturulma tarihi.
"""


class Counties(models.Model):
    name = models.CharField(max_length=20, default='', null=False, blank=False)
    city = models.ForeignKey(Cities)
    cdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Users(models.Model):
    SEX = (
        (False, _(u'KADIN')),
        (True, _(u'ERKEK')),
    )
    user = models.ForeignKey(User)
    profile_photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/")
    sex = models.BooleanField(null=False, choices=SEX, blank=False, default=True)
    birthday = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=11, default='', null=True, blank=True)
    iban = models.CharField(max_length=34, default='', null=True, blank=True)
    profession = models.CharField(max_length=30, default='', null=True, blank=True)
    account_holder = models.CharField(max_length=50, default='', null=True, blank=True)
    balance = models.DecimalField(default=1, null=False, blank=False, max_digits=8, decimal_places=2)
    county = models.ForeignKey(Counties, null=True, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    to = models.ForeignKey(User, related_name="to")
    title = models.CharField(max_length=180, default='', null=False, blank=False)
    cdate = models.DateTimeField(auto_now_add=True)


class MessageContent(models.Model):
    message = models.ForeignKey(Message, related_name="Message")
    title = models.CharField(max_length=1000, default='', null=False, blank=False)
    cdate = models.DateTimeField(auto_now_add=True)


class AccountProcess(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=180, default='', null=True, blank=True)
    was_paid_price = models.DecimalField(default=1, null=False, blank=False, max_digits=8, decimal_places=2)
    cdate = models.DateTimeField(auto_now_add=True)


class ArticleType(models.Model):
    name = models.CharField(max_length=180, default='', null=True, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    user = models.ForeignKey(User, blank=True, default=None, null=True)
    title = models.CharField(max_length=180, default='', null=True, blank=True)
    description = models.CharField(max_length=180, default='', null=True, blank=True)
    key_word = models.CharField(max_length=500, default='', null=True, blank=True)
    word_number = models.PositiveSmallIntegerField(default=1, null=False, blank=False)
    price = models.DecimalField(default=1, null=False, blank=False, max_digits=8, decimal_places=2)
    is_urgent = models.BooleanField(null=False, blank=False, default=False)
    is_finished = models.BooleanField(null=False, blank=False, default=False)
    is_approved = models.BooleanField(null=False, blank=False, default=False)
    article_type = models.ForeignKey(ArticleType, null=True, blank=True)
    was_paid_price = models.DecimalField(default=1, null=False, blank=False, max_digits=8, decimal_places=2)
    cdate = models.DateTimeField(auto_now_add=True)

