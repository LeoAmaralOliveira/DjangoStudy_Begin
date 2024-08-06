from django.contrib import admin
from apps.gallery.models import Photography


class ListingPhotography(admin.ModelAdmin):
    list_display = ("id", "name", "label", "published")
    list_display_links = ("id", "name", "label")
    search_fields = ("name",)
    list_filter = ("category", "user")
    list_editable = ("published",)
    list_per_page = 10


admin.site.register(Photography, ListingPhotography)
