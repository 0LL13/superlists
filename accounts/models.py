import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib import auth
from django.db import models


auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(AbstractBaseUser):
    pass


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)


# class User(models.Model):  # doesnt work
# class User(Auth_user):
#
#     # email = models.EmailField(primary_key=True)  # doesnt work
#
#     def __init__(self, **kwds):
#         email = self.email(primary_key=True)
#         REQUIRED_FIELDS = []
#         USERNAME_FIELD = 'email'
#         is_anonymous = False
#         is_authenticated = True
#         kwds = (email, REQUIRED_FIELDS, USERNAME_FIELD, is_anonymous, is_authenticated,)  # noqa
#
#         super().__init__(**kwds)
