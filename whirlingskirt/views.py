from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from accounts.models import Account
from utils.decorators import anonymous_required
from accounts.forms import SignUpForm



@anonymous_required
def home(request):
    return render(request, 'home.html', {})


@anonymous_required
def login_view(request):
    errors = []
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            errors.append("Combination email/password is invalid")
    return render(request, 'login.html', {'errors': errors})


@anonymous_required
def signup(request):
    invited_by = None
    if request.method == 'GET':
        invited_by_id = request.GET.get('invited_by', None)
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        invited_by_id = request.POST.get('invited_by', None)
        if form.is_valid():
            if invited_by_id:
                try:
                    invited_by = Account.objects.get(pk=invited_by_id)
                except Account.DoesNotExist:
                    pass
            Account.objects.create_user(
                form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                invited_by=invited_by
            )
            new_user = authenticate(email=request.POST['email'],
                                    password=request.POST['password'])
            login(request, new_user)
            return HttpResponseRedirect('/dashboard/')
    if invited_by_id:
        try:
            invited_by_obj = Account.objects.get(pk=invited_by_id)
        except Account.DoesNotExist:
            pass
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