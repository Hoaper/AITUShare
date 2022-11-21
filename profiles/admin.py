from django.contrib import admin
from .models import profiles

admin.site.register(profiles.Profile)
admin.site.register(profiles.Verification)
