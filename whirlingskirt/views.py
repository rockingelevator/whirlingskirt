from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def invite(request):
    return render(request, 'invite.html', {})


def customers(request):
    return render(request, 'customers.html', {})