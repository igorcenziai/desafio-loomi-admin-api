from django.contrib import admin
from .models import Tinta

# Register your models here.
@admin.register(Tinta)
class TintaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cor', 'tipo_parede', 'ambiente', 'acabamento', 'linha')
    search_fields = ('nome', 'cor', 'tipo_parede', 'ambiente', 'acabamento', 'linha')
    list_filter = ('tipo_parede', 'ambiente', 'acabamento', 'linha')
    ordering = ('nome',)
    list_per_page = 20
