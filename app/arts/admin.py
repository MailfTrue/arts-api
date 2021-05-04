from django.contrib import admin
from app.admin import site
from app.arts.models import ArtWork


@admin.register(ArtWork, site=site)
class ArtWorkAdmin(admin.ModelAdmin):
    list_display = 'title', 'type',
    list_filter = 'type',
