# -*- coding: utf-8 -*-

from datetime import datetime
from logging import getLogger

from .models import User

log = getLogger("django")


class AuthBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            log.debug("El email no es válido")
            return None

        if user.check_password(password):
            user.last_login = datetime.now()
            user.save()
            return user
        log.debug("La contraseña es incorrecta")
        return None

    def get_user(self, pk):
        log.debug("get_user: {0}".format(pk))
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            log.debug("El usuario no existe")
            return None
