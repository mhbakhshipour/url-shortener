from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password

from client.models import User


@require_http_methods(['GET', "POST"])
def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/create-short-link')
        else:
            return render(request, 'auth/register.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            if 'requestedurl' in request.session.keys():
                return redirect(request.session['requestedurl'])
            else:
                return redirect('/create-short-link')
        else:
            email = request.POST.get('email', None)
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            try:
                user = User.objects.create(
                    email=email, first_name=first_name, last_name=last_name, username=username)
                user.password = make_password(password)
                user.save(update_fields=["password"])
            except:
                context = {"msg": "Please check username"}
                return render(request, 'auth/register.html', context)

            auth_login(request, user)

            if 'requestedurl' in request.session.keys():
                return redirect(request.session['requestedurl'])
            else:
                context = {"msg": f"SUCCESS, Hi {user.username}"}
                return render(request, 'auth/register.html', context)
