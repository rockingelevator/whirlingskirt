from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from accounts.models import Account, ServiceProvider
from transactions.models import Balance, Payment, Booking
from invites.models import Invite
from utils.decorators import anonymous_required
from accounts.forms import SignUpForm
from utils.transactions import BONUSES


@anonymous_required
def home(request):
    return render(request, 'home.html', {})


@anonymous_required
def login_view(request):
    errors = []
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        account = authenticate(email=email, password=password)
        if account is not None:
            request.session['account_id'] = account.id
            login(request, account)
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
    my_id = request.session.get('account_id', '')
    if not my_id:
        return HttpResponseRedirect('/logout/')
    try:
        my = Account.objects.get(pk=my_id)
    except Account.DoesNotExist:
        return HttpResponseRedirect('/logout/')
    else:

        # declaring defaults
        current_balance, currency, total_revenue = 0, '', 0

        # current balance
        try:
            balance = Balance.objects.get(account=my)
        except Balance.DoesNotExist:
            pass
        else:
            current_balance = balance.current_balance
            currency = balance.currency

        # total revenue
        payments = Payment.objects.filter(account=my)
        total_revenue = sum([x['value'] for x in payments])

        # invites
        invites = Invite.objects.filter(author=my)
        invites_count = invites.count()

        # members
        members = Account.objects.filter(invited_by=my).annotate(transactions=Count('booking'))
        members_count = members.count()

        # active members
        active_members = sum([1 for x in members if x.transactions > 0])

        # service providers
        service_providers = ServiceProvider.objects.filter(owner__in=members)
        service_providers_count = service_providers.count()

        # conversion_rate
        conversion_rate = 0 if invites_count == 0 else ((members_count + service_providers_count)/invites_count) * 100

        # transactions
        members_transactions = Booking.objects.filter(account__in=members)

        # return from each transactions: 20% from commission if transaction value more than bonus
        # or 2% from transaction value if it's less than our bonus
        members_transactions_total_bonus = sum([(x['value']*BONUSES['commission']['for_booking'])/100 if x['value'] < BONUSES['for']['member'] else BONUSES['for']['member']*BONUSES['commission']['for_provision']/100 for x in members_transactions])
        sp_transactions = Booking.objects.filter(service_provider__in=service_providers).exclude(account__in=members)
        sp_transactions_total_bonus = sum([(x['value']*BONUSES['commission']['for_booking'])/100 if x['value'] < BONUSES['for']['sp'] else BONUSES['for']['sp']*BONUSES['commission']['for_provision']/100 for x in sp_transactions])

        # payments
        payments = Payment.objects.filter(account=my).values('value', 'transaction_date')

        return render(request, 'dashboard.html', {
            'my': {
                'full_name': "%s %s" % (my.first_name, my.last_name),
            },
            'balance': {
                'currency': currency,
                'current': current_balance,
                'total_revenue': total_revenue
            },
            'invites': {
                'count': invites_count,
                'members_registrations': members_count,
                'sp_registrations': service_providers_count,
                'total_registrations': members_count + service_providers_count,
                'conversion_rate': conversion_rate,
                'active_members': active_members
            },
            'transactions': members_transactions.count() + sp_transactions.count(),
            'bonuses': {
                'for_members': members_transactions_total_bonus,
                'for_members_percent': int((members_transactions_total_bonus * members_count * BONUSES['for']['member'])/100),
                'for_service_providers': sp_transactions_total_bonus,
                'for_service_providers_percent': int((sp_transactions_total_bonus * service_providers_count * BONUSES['for']['sp'])/100)
            },
            'potential_income': {
                'for_service_providers': service_providers_count * BONUSES['for']['sp'],
                'for_members': members_count * BONUSES['for']['member']
            },
            'payments': payments
        })


def invite(request):
    return render(request, 'invite.html', {})


def customers(request):
    return render(request, 'customers.html', {})