from django.contrib import admin
from django.utils.html import format_html
from .models import CallbackRequest


@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "service_badge",
        "created_at",
    )

    list_filter = ("service","created_at")

    search_fields = ("name","email","phone")

    ordering = ("-created_at",)

    list_per_page = 15


    def service_badge(self,obj):

        color="blue"

        if obj.service=="Accounting":
            color="green"

        if obj.service=="Taxation":
            color="orange"

        if obj.service=="General Inquiry":
            color="gray"

        return format_html(
        '<span style="background:{};color:white;padding:5px 10px;border-radius:6px;">{}</span>',
        color,
        obj.service
        )

    service_badge.short_description="Service"