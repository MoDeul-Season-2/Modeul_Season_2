from django.contrib import admin
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):

    list_display = ("name", "city", "address", "price",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass