from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate


@require_http_methods(['GET', "POST"])
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/create-short-link')
        else:
            return render(request, 'auth/login.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            if 'requestedurl' in request.session.keys():
                return redirect(request.session['requestedurl'])
            else:
                return redirect('/create-short-link')
        else:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                if 'requestedurl' in request.session.keys():
                    return redirect(request.session['requestedurl'])
                else:
                    context = {"msg": f"SUCCESS, Hi {user.username}"}
                return render(request, 'auth/login.html', context)
            else:
                context = {"msg": "Please check username or password"}
                return render(request, 'auth/login.html', context)
