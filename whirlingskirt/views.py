from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.decorators import anonymous_required


@anonymous_required
def home(request):
    return render(request, 'home.html', {})


@anonymous_required
def login(request):
    return render(request, 'login.html', {})


@anonymous_required
def signup(request):
    return render(request, 'signup.html', {})


def logout(request):
    return render(request, 'home.html', {})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})


def invite(request):
    return render(request, 'invite.html', {})


def customers(request):
    return render(request, 'customers.html', {})