from django.contrib import admin
from . import models


admin.site.register(models.WorkTime)
# admin.site.register(models.Profile)
admin.site.register(models.Employee)
admin.site.register(models.Food)

