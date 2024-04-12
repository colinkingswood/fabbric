from django.contrib import admin
from prototype.models import ClothingItem
# Register your models here.

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "color"]
