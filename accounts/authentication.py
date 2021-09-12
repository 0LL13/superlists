from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        print('authenticating - this is uid:', uid)
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            print('token does not exist')
            print('uid:', uid)
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
