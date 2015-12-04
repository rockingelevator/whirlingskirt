from django.contrib import admin
from .models import Booking, Payment, Balance

admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Balance)
