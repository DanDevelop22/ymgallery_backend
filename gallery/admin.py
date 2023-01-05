from django.contrib import admin
from .models import Paint
@admin.register(Paint)
class PaintAdmin(admin.ModelAdmin):
    list_display = ('name','img','author','price')
