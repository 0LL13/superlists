import inspect

from django.contrib import auth, messages
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import redirect

from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email],
        fail_silently=False,
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    print()
    print('inspecting calling function:', inspect.stack()[1].function)
    print('request:', request)
    print('user:', user)
    print('request.GET.get("token"):', request.GET.get('token'))
    if user:
        print('authenticating')
        auth.login(request, user)
    else:
        print('no user, no login')
    return redirect('/')
