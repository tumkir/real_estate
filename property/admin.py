from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", )
    search_fields = ("town", "address", "owner")
    list_display = ("address", "price", "new_building", "construction_year", "town")
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony")
    raw_id_fields = ('likes', )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", )
    search_fields = ("user", "flat")
    list_display = ("user", "flat", "complaint_text")
