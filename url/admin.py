from django.contrib import admin

from url.models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ("creator", "short_url_id")
    search_fields = ("creator", "orginal_url")
    autocomplete_fields = ("creator",)
