from django.contrib import admin
from subscriptions.models import CustomUser, Package, Subscription

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Package)
admin.site.register(Subscription)
