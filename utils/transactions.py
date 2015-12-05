# utils/transaction.py

CURRENCIES = (
    ("eur", "€"),
    ("usd", "$"),
    ("uah", "₴")
)

BONUSES = {
    'currency': CURRENCIES[0],
    'for': {
        'sp': 500,
        'member': 10
    },
    'commission': {
        'from_provision': 20,
        'from_booking': 2
    }
}