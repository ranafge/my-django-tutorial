from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.People)
admin.site.register(models.PeopleGame)
admin.site.register(models.Game)