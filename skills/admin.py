from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "provider", "category", "price", "location", "is_available", "created_at")
    list_filter = ("category", "is_available")
    search_fields = ("title", "provider__email", "location")