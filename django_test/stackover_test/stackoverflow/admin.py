from django.contrib import admin
from . import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("text", 'get_author',)

    def get_author(self, obj):
        return obj.author.username

    get_author.short_description = 'POst Author Name'  # header section of the column
    # get_author.admin_order_field = 'author'


# itemmodel readony field
# Itemadmin is work fine.
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ['sku']
    # disable add model
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(models.Applicant)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Work)
admin.site.register(models.Part)
admin.site.register(models.Pattern)
admin.site.register(models.Post, UserAdmin)
admin.site.register(models.A)
admin.site.register(models.B)
admin.site.register(models.C)
admin.site.register(models.Comment)
admin.site.register(models.Person)
admin.site.register(models.PersonScore)
admin.site.register(models.PersonType)
admin.site.register(models.Room)
