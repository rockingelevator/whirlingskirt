from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from accounts.models import Account
from utils.decorators import anonymous_required
from accounts.forms import SignUpForm



@anonymous_required
def home(request):
    return render(request, 'home.html', {})


@anonymous_required
def login(request):
    return render(request, 'login.html', {})


@anonymous_required
def signup(request):
    invited_by = {}
    if request.method == 'GET':
        invited_by_id = request.GET.get('invited_by', None)
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        invited_by_id = request.POST.get('invited_by', None)
        if form.is_valid():
            print('Valid!')
            print(request.POST)
            return HttpResponseRedirect('/dashboard/')
    if invited_by_id:
        try:
            invited_by_obj = Account.objects.get(pk=invited_by_id)
        except Account.DoesNotExist:
            print('No such user')
        else:
            invited_by = {
                'user_id': invited_by_obj.id,
                'full_name': invited_by_obj.first_name + ' ' + invited_by_obj.last_name
            }
    return render(request, 'signup.html', {'form': form, 'invited_by': invited_by})


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