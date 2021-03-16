from django.contrib import admin
from . import models


@admin.register(models.Apply)
class ApplyAdmin(admin.ModelAdmin):

    list_display = ("applyName", "house", "host", "guest", "price",)