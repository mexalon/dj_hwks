from django.contrib import admin
from .models import Advertisement, AdvertisementStatusChoices


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
