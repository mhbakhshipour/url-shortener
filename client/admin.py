from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from client.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("phone_number",)
    search_fields = UserAdmin.search_fields + ("phone_number",)
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] += ("phone_number",)
    list_filter = UserAdmin.list_filter
