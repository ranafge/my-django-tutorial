from django.contrib import admin
from . import models

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(models.Profile, ProfileAdmin)