from accounts.models import Token
# from accounts.authentication import PasswordlessAuthenticationBackend as PAB  # not in book  # noqa
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import redirect


def send_login_email(request):
    email = request.POST['email']
    # print(type(send_mail))
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    print('url from send_login_email:', url)
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login_w_email_token(request):
    username = 'anonymous'
    password = 'no password'
    token = request.GET.get('token')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
    return 'invalid login'


# doesnt work
# def login(request):
#     print('login request:', request)
#     print('request.GET.get(token):', request.GET.get('token'))
#     user = auth.authenticate(uid=request.GET.get('token'))  # doesn't work
#     # user = PAB().authenticate(uid=request.GET.get('token'))  # doesn't work either  # noqa
#     print(type(user))
#     print(user)
#     if user:
#         auth.login(request, user)
#     return redirect('/')
