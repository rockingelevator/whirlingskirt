from django import template
from transactions.models import CURRENCIES

register = template.Library()

@register.filter
def currency(q):
    for choice in CURRENCIES:
        if choice[0] == q:
            return choice[1]
    return ''
