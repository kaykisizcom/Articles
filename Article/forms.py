from django.contrib.auth.models import User
from Article.models import Users

__author__ = 'mehmet'


class new_user_form(forms.ModelForm):
    class Meta:
        model = User
        widgets = {}


class new_users_form(forms.ModelForm):
    class Meta:
        model = Users
        widgets = {}