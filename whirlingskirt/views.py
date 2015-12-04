from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from utils.decorators import anonymous_required



@anonymous_required
def home(request):
    return render(request, 'home.html', {})


@anonymous_required
def login(request):
    return render(request, 'login.html', {})


@anonymous_required
def signup(request):
    invited_by_id = request.GET.get('invited_by', None)
    invited_by = ''
    res = {}
    if invited_by_id:
        try:
            invited_by = User.objects.get(pk=invited_by_id)
        except User.DoesNotExist:
            print('No such user')
        else:
            res['invited_by'] = invited_by.first_name + ' ' + invited_by.last_name

    return render(request, 'signup.html', res)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})


def invite(request):
    return render(request, 'invite.html', {})


def customers(request):
    return render(request, 'customers.html', {})